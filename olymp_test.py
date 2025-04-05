# olymp_login_debug.py

import logging
from olymptradeapi.stable_api import Olymptrade

# Enable debug logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

# Credentials
EMAIL = "artechnoteam@gmail.com"
PASSWORD = "Ankit@123"
SESSION_ID = "1000869312323232143243243243234432"  # Replace with real one

# Olymp Trade login
print("🔐 Logging in...")

try:
    account = Olymptrade(EMAIL, PASSWORD, set_ssid=SESSION_ID)
    connected, response = account.connect()

    if connected:
        print("✅ Login Success!")
    else:
        print("❌ Login Failed!")
        print("Reason:", response)

except Exception as e:
    print("🚨 Error occurred:", str(e))
