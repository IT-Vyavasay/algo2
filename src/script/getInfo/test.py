import sys
import os

# Add the parent directory (LIVE_FEED) to the system path for package discovery
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.kotak_neo_api_main.neo_api_client.neo_api import NeoAPI
from utils.constant import CONSUMER_KEY, MOBILE, UCC, MPIN, TOTP,CONSUMER_SECRET, ENVIRONMENT, FIN_KEY, MCX_GOLD_TOKEN, PASSWORD, NEO_ACCESS_TOKEN
 
 
def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_close(message):
    print(message)
    
def on_open(message):
    print(message)
    
#on_message, on_open, on_close and on_error is a call back function we will provide the response for the subscribe method.
# access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
# environment by default uat you can pass prod to connect to live server
client = NeoAPI(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, environment='uat',
                access_token=None, neo_fin_key=None)

# Initiate login by passing any of the combinations mobilenumber & password (or) pan & password (or) userid & password
# Also this will generate the OTP to complete 2FA
client.login(mobilenumber=MOBILE, password=MPIN)

# Complete login and generate session token

otp_num = input("Enter OTP : ")
client.session_2fa(OTP=otp_num)
print("Session successfully")
# Setup Callbacks for websocket events (Optional)
client.on_message = on_message  # called when message is received from websocket
client.on_error = on_error  # called when any error or exception occurs in code or websocket
client.on_close = on_close  # called when websocket connection is closed
client.on_open = on_open  # called when websocket successfully connects