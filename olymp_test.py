# olymp_login_test.py

from olymptradeapi.stable_api import Olymptrade

# अपने credentials यहाँ भरें
EMAIL = "artechnoteam.com"
PASSWORD = "Ankit@123"
SESSION_ID = "1000869312323232143243243243234432"

# login_app.py

import streamlit as st
from olymptradeapi.stable_api import Olymptrade

st.set_page_config(page_title="Olymp Trade Login", page_icon="🔐")

st.title("🔐 Olymp Trade Session Login Test")

# Input: Session ID
session_id = st.text_input("1000869312323232143243243243234432", type="password")

# Login button
if st.button("Login to Olymp Trade"):
    if not session_id.strip():
        st.error("⚠️ Please enter a valid Session ID.")
    else:
        try:
            account = Olymptrade(set_ssid=session_id)
            connected, response = account.connect()
            
            if connected:
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Login Failed")
                st.text(f"Reason: {response}")
        except Exception as e:
            st.exception(f"🚨 Error: {e}")

