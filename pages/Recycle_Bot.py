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

# --------------------------
# 2. Load Environment Variables
# --------------------------
#load_dotenv(r"C:\streamlit_projects\myenv\.env")
# Load the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["openai_api_key"]

if not openai_api_key:
    st.error("OpenAI API key not found. Please ensure it is properly set in the secrets.toml file.")
    st.stop()

# # Function to check password
# def check_password():
#     """Check for a password input."""
#     password = st.text_input("Password", type="password")
#     if password == "your_password":  # Replace with your actual password
#         return True
#     else:
#         st.warning("Incorrect password!")
#         return False


# Function to scrape recyclable materials from multiple NEA pages
@st.cache_data(ttl=3600)  # Cache data for 1 hour
def scrape_nea_data():
    urls = [
        "https://www.nea.gov.sg/our-services/waste-management/recycling",
        "https://www.nea.gov.sg/our-services/waste-management/recycling/what-can-i-recycle",
        "https://www.nea.gov.sg/our-services/waste-management/recycling/recycling-facilities"
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
    st.title("NEA Recycling Chatbot")
    
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
