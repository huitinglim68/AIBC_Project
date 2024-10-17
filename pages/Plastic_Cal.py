import streamlit as st
import time

# Define the conversion factors for plastic waste (in kg)
PLASTIC_BOTTLE_WASTE_PER_YEAR = 0.012  # kg per bottle per week
PLASTIC_BAG_WASTE_PER_YEAR = 0.002  # kg per bag per week
PLASTIC_PACKAGE_WASTE_PER_YEAR = 0.01  # kg per package per week

# Function to calculate plastic footprint
def calculate_plastic_footprint(bottles_per_week, bags_per_week, packages_per_week):
    # Calculate annual plastic waste from each category
    annual_bottle_waste = bottles_per_week * PLASTIC_BOTTLE_WASTE_PER_YEAR * 52
    annual_bag_waste = bags_per_week * PLASTIC_BAG_WASTE_PER_YEAR * 52
    annual_package_waste = packages_per_week * PLASTIC_PACKAGE_WASTE_PER_YEAR * 52

    # Sum all categories to get total annual plastic waste
    total_annual_plastic_waste = annual_bottle_waste + annual_bag_waste + annual_package_waste
    return total_annual_plastic_waste

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

# Add an image banner (optional)
# st.image("https://www.example.com/your-banner-image.jpg", use_column_width=True)  # Replace with your own image link

# Title and description
st.markdown("# 🌍 Plastic Footprint Calculator")
st.markdown("Estimate your annual plastic footprint based on your weekly plastic usage.")

# Sidebar inputs
st.sidebar.title("Plastic Usage Inputs")
bottles_per_week = st.sidebar.number_input("Plastic bottles per week", min_value=0, value=0, step=1)
bags_per_week = st.sidebar.number_input("Plastic bags per week", min_value=0, value=0, step=1)
packages_per_week = st.sidebar.number_input("Plastic packages per week", min_value=0, value=0, step=1)

# Main page description
st.markdown("## 🛍️ Input your weekly plastic usage and see the results below.")

# Calculate the footprint and show results when button is clicked
if st.button("Calculate Footprint"):
    total_footprint = calculate_plastic_footprint(bottles_per_week, bags_per_week, packages_per_week)
    
    # Progress bar animation
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    
    # Display the result
    st.success(f"Your estimated annual plastic footprint is **{total_footprint:.2f} kg**.")

    # Extra metric for a quick highlight
    st.metric("Total Plastic Waste (kg/year)", f"{total_footprint:.2f} kg")
