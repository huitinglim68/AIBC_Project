import streamlit as st

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
    
    .stTextInput, .stNumberInput input {
        border-radius: 5px;
        padding: 10px;
        border: 2px solid #6C63FF;
    }
    
    .stMarkdown {
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Call the function to apply custom CSS
custom_css()

# Title and banner
st.title("Project Overview:Plastic Footprint Calculator & Recycling Chatbot")

# Project Scope
st.markdown("## 📊 Project Scope")
st.markdown("""
This project consists of two main components: the **Plastic Footprint Calculator**and the **Recycling Chatbot**. 
The calculator estimates the user's annual plastic footprint based on their weekly plastic usage while the chatbot aims to provide users with information about recyclable materials in Singapore.
""")

# Objectives
st.markdown("## 🎯 Objectives")
st.markdown("""

- **Plastic Footprint Calculator**: 
  - To help users assess their plastic usage and its impact on the environment.
  - To raise awareness about plastic consumption.
  
- **Recycling Chatbot**: 
  - To assist users in understanding what materials are recyclable in Singapore.
  - To provide quick and accurate responses to user inquiries regarding recycling.

""")

# Data Sources
st.markdown("## 📚 Data Sources")
st.markdown("""
- **NEA Website**: 
  - The data for recyclable materials is sourced from multiple pages on the National Environment Agency (NEA) website, including:
    - [Donation, Resale and Repair Channels](https://www.nea.gov.sg/our-services/waste-management/donation-resale-and-repair-channels)
    - [Waste Collection Systems](https://www.nea.gov.sg/our-services/waste-management/waste-collection-systems)
    - [Types of recyclables and recycling processes](https://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/types-of-recyclables-and-recycling-processes)
  
- **Plastic Footprint Estimates**: 
  - Estimated annual waste factors for different types of plastic products are used to calculate the plastic footprint.
""")

# Features
st.markdown("## 🛠️ Features")
st.markdown("""
- **NEA Recycling Chatbot**:
  - User-friendly interface to ask questions about recycling.
  - Quick retrieval of information on recyclable materials through a language model.
  
- **Plastic Footprint Calculator**:
  - Input fields to estimate weekly plastic usage for bottles, bags, and packages.
  - Calculation of total annual plastic waste with an animated progress bar.
  - Metrics to display total plastic waste in a visually appealing format.
""")

st.markdown("##Disclaimer")
st.markdown("""
IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.
""")
