import sys
import os

# Add the parent directory (LIVE_FEED) to the system path for package discovery
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from neo_api_client import NeoAPI
from utils.constant import CONSUMER_KEY, MOBILE, UCC, MPIN, TOTP, ENVIRONMENT, FIN_KEY, MCX_GOLD_TOKEN, PASSWORD, NEO_ACCESS_TOKEN

print("initialize")
client = NeoAPI(environment='prod', access_token=None, neo_fin_key=None, consumer_key=CONSUMER_KEY)

print("client created")

# Step 1: Login TOTP → generates view_token
totp_num = input("Enter totp: ")
client.totp_login(mobile_number=MOBILE, ucc=UCC, totp=totp_num)
print("TOTP login successful")

# Step 2: Validate MPIN → prepares trade token
client.totp_validate(MPIN)
print("MPIN validated")

# Step 3: Generate session token (trade token)
session_res = client.session_token()
print("Session token generated:", session_res)

# Step 4: Now call your protected API
print("Calling trade report...")
res = client.trade_report()
print("Response:", res)
