import sys
import os

# Add the parent directory (LIVE_FEED) to the system path for package discovery
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.kotak_neo_api_main.neo_api_client.neo_api import NeoAPI
from utils.constant import CONSUMER_KEY, MOBILE, UCC, MPIN, TOTP, ENVIRONMENT, FIN_KEY, MCX_GOLD_TOKEN, PASSWORD, NEO_ACCESS_TOKEN
 