from pyquotex.api import Quotex

# Login Info (email और password यहां भरें)
EMAIL = "traderankit93.com"
PASSWORD = "Ankit@123"

q = Quotex(email=EMAIL, password=PASSWORD)

# लॉगिन करें
login_success = q.connect()

if login_success:
    print("✅ Login Success (Demo)")
else:
    print("❌ Login Failed")
