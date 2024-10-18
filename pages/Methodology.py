import streamlit as st

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
