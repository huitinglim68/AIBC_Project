import streamlit as st
import hmac

def check_password():
    secret_password = st.secrets["password"]["password"]
    user_password = st.text_input("Enter your password", type="password")
    
    if user_password:
        if hmac.compare_digest(user_password, secret_password):
            return True
        else:
            st.error("Access Denied")
            return False
    return False
