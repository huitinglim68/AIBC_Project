import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv
import logging
from helper_functions.utility import check_password  # Import the check_password function

# # Password check at the start of the app
if not check_password():
    st.stop()
    
# 1. Configure Logging
# --------------------------
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# --------------------------
# 2. Load Environment Variables
# --------------------------
#load_dotenv(r"C:\streamlit_projects\myenv\.env")
# Load the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["openai_api_key"]

if not openai_api_key:
    st.error("OpenAI API key not found. Please ensure it is properly set in the secrets file.")
    st.stop()
# Custom CSS for styling
def custom_css():
    st.markdown("""
    <style>
    /* Add custom fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        color: #333;
    }
    
    h1, h2, h3 {
        color: #6C63FF;
    }
    
    .stButton button {
        background-color: #6C63FF;
        color: white;
        font-size: 18px;
        border-radius: 8px;
    }
    
    .stNumberInput input {
        border: 2px solid #6C63FF;
        border-radius: 5px;
    }
    
    .stTextInput {
        border-radius: 5px;
        padding: 10px;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Call the function to apply custom CSS
custom_css()

# Function to scrape recyclable materials from multiple NEA pages
@st.cache_data(ttl=3600)  # Cache data for 1 hour
def scrape_nea_data():
    urls = [
        "https://www.nea.gov.sg/our-services/waste-management/donation-resale-and-repair-channels",
        "https://www.nea.gov.sg/our-services/waste-management/waste-collection-systems",
        "https://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/types-of-recyclables-and-recycling-processes"
    ]
    recyclable_materials = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for item in soup.find_all('li'):  # Adjust tag based on website structure
            text = item.get_text(strip=True)
            if text:
                recyclable_materials.append(text)
    
    return recyclable_materials

# Initialize OpenAI components (Embeddings and Language Model)
def init_openai():
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    return embeddings, llm

# Create FAISS vector store from the scraped data
def create_vector_store(materials, embeddings):
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_text("\n".join(materials))
    vectorstore = FAISS.from_texts(documents, embeddings)
    return vectorstore

# Set up the RetrievalQA Chain
def setup_qa_chain(vectorstore, llm):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    return qa_chain

# Main Streamlit app
def main():
    st.title("Recycling Chatbot")
    
    # Add a subheader for better organization
    st.subheader("Ask any question about recyclable materials in Singapore!")

    # Scrape the data from NEA
    materials = scrape_nea_data()
    
    # Initialize OpenAI and FAISS vector store
    embeddings, llm = init_openai()
    vectorstore = create_vector_store(materials, embeddings)

    # Set up the QA chain
    qa_chain = setup_qa_chain(vectorstore, llm)

    # Create two columns for a better layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Use a larger text area for user input
        user_input = st.text_area(
            "Enter your question here:",
            placeholder="e.g., Can I recycle plastic bottles?",
            height=150,  # Adjust height for a bigger input area
            key="query"
        )
    
    # Move button and answer output below the input box
    if st.button("Get Answer") or (st.session_state.query and st.session_state.query.strip()):
        if user_input.strip() and qa_chain:
            with st.spinner("Fetching answer..."):
                result = qa_chain({"query": user_input})
                if 'result' in result and result['result']:
                    st.write(result['result'])
                else:
                    st.write("I'm not sure about that. You might want to ask something more specific!")
        else:
            st.warning("Please enter a valid question.")

if __name__ == "__main__":
    main()
