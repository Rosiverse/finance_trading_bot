import os
import time
import hashlib
import hmac
from urllib.parse import urlencode
import requests
from dotenv import load_dotenv
from bot.logging_config import logger

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

# THIS IS REAL MONEY (Danger)
# BASE_URL = "https://fapi.binance.com""

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        if not self.api_key or not self.api_secret:
            logger.error("API credentials missing. Please set BINANCE_API_KEY and BINANCE_API_SECRET.")
            raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET must be set in environment variables.")

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def send_signed_request(self, method: str, endpoint: str, **kwargs):
        url = f"{BASE_URL}{endpoint}"
        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        params = kwargs.get("params", {})
        
        params['timestamp'] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        params['signature'] = signature

        try:
            logger.info(f"Sending {method} request to {endpoint}")
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, params=params)
            else:
                raise ValueError("Unsupported HTTP method")

            data = response.json()
            
            if response.status_code not in [200, 201] or ('code' in data and data['code'] != 200):
                error_msg = data.get('msg', 'Unknown API Error')
                if 'code' in data and data['code'] < 0:
                    logger.error(f"Binance API Error - Code: {data['code']}, Message: {error_msg}")
                    raise Exception(f"Binance API Error [{data['code']}]: {error_msg}")
                response.raise_for_status()

            logger.info("Request successful.")
            return data

        except requests.exceptions.RequestException as req_err:
            logger.error(f"Network error occurred: {req_err}")
            raise Exception(f"Network error: {req_err}")
        except ValueError as json_err:
            logger.error(f"Failed to parse JSON response: {json_err}")
            raise Exception("Invalid JSON response received from API")
