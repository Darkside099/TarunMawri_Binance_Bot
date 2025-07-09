import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY: str = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET: str = os.getenv("BINANCE_API_SECRET")
BASE_URL: str = "https://testnet.binancefuture.com"
