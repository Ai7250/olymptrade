# olymp_login_test.py

from olymptradeapi.stable_api import Olymptrade

# अपने credentials यहाँ भरें
EMAIL = "artechnoteam.com"
PASSWORD = "Ankit@123"
SESSION_ID = "1000869312323232143243243243234432"

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
