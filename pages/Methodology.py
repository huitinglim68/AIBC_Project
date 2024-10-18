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

# Set the title of the Streamlit app
st.title("Methodology")

# Section for Plastic Footprint Calculator
st.markdown("### **Plastic Footprint Calculator**")

# Add space using HTML line break
st.markdown("<br>", unsafe_allow_html=True)

# Insert Image 1
st.image("images/Flow Chart 1.PNG", caption="Flow Chart 1", use_column_width=True)

# Section for Recycling Bot
st.markdown("### ** Recycling Bot**")

# Add space using HTML line break
st.markdown("<br>", unsafe_allow_html=True)

# Insert Image 2
st.image("images/Flow Chart 2.PNG", caption="Flow Chart 2", use_column_width=True)
