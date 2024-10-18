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
st.title("Project Overview: NEA Recycling Chatbot & Plastic Footprint Calculator")
# st.image("https://www.example.com/your-banner-image.jpg", use_column_width=True)  # Replace with your own image link

# Project Scope
st.markdown("## 📊 Project Scope")
st.markdown("""
This project consists of two main components: the **NEA Recycling Chatbot** and the **Plastic Footprint Calculator**. 
The chatbot aims to provide users with information about recyclable materials in Singapore, while the calculator estimates the user's annual plastic footprint based on their weekly plastic usage.
""")

# Objectives
st.markdown("## 🎯 Objectives")
st.markdown("""
- **NEA Recycling Chatbot**: 
  - To assist users in understanding what materials are recyclable in Singapore.
  - To provide quick and accurate responses to user inquiries regarding recycling.
  
- **Plastic Footprint Calculator**: 
  - To help users assess their plastic usage and its impact on the environment.
  - To raise awareness about plastic consumption and promote sustainable practices.
""")

# Data Sources
st.markdown("## 📚 Data Sources")
st.markdown("""
- **NEA Website**: 
  - The data for recyclable materials is sourced from multiple pages on the National Environment Agency (NEA) website, including:
    - [Recycling Overview](https://www.nea.gov.sg/our-services/waste-management/recycling)
    - [What Can Be Recycled](https://www.nea.gov.sg/our-services/waste-management/recycling/what-can-i-recycle)
    - [Recycling Facilities](https://www.nea.gov.sg/our-services/waste-management/recycling/recycling-facilities)
  
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
