# olymp_login_test.py

from olymptradeapi.stable_api import Olymptrade

# अपने credentials यहाँ भरें
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
SESSION_ID = "your_session_cookie_here"

# Olymptrade object बनाएं
account = Olymptrade(EMAIL, PASSWORD, set_ssid=SESSION_ID)

# Connect करें
connected, response = account.connect()

# Login status print करें
if connected:
    print("✅ Login Success!")
else:
    print("❌ Login Failed!")
    print("Reason:", response)
