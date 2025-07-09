from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from logger import logger
from utils import validate_symbol, validate_order_side, validate_quantity


def place_market_order(symbol: str, side: str, quantity: str):
    if not all([
        validate_symbol(symbol),
        validate_order_side(side),
        validate_quantity(quantity)
    ]):
        logger.error(f"Invalid input: {symbol}, {side}, {quantity}")
        return "Invalid input"

    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=float(quantity)
        )
        logger.info(f"Market order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Market order error: {e}")
        return f"Error placing market order: {e}"