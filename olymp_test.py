

import streamlit as st
from pyquotex.api import Quotex

st.set_page_config(page_title="Quotex Login Test", page_icon="🔐")

st.title("🔐 Quotex Demo Account Login Tester")

# Input fields
email = st.text_input("📧traderankit93.com")
password = st.text_input("🔑Ankit@123", type="password")

# Button to attempt login
if st.button("🚀 Login to Demo"):
    if not email or not password:
        st.warning("⚠️ Please enter both email and password.")
    else:
        try:
            qx = Quotex(email=email, password=password)
            if qx.connect():
                st.success("✅ Login Successful (Demo Account)")
            else:
                st.error("❌ Login Failed — Wrong credentials or network error.")
        except Exception as e:
            st.error(f"🚨 Error during login: {str(e)}")
