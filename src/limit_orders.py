from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from logger import logger
from utils import validate_symbol, validate_order_side, validate_quantity


def place_limit_order(symbol: str, side: str, quantity: str, price: str):
    if not all([
        validate_symbol(symbol),
        validate_order_side(side),
        validate_quantity(quantity)
    ]):
        logger.error(f"Invalid input: {symbol}, {side}, {quantity}, {price}")
        return "Invalid input"

    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            quantity=float(quantity),
            price=str(price),
            timeInForce="GTC"
        )
        logger.info(f"Limit order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Limit order error: {e}")
        return f"Error placing limit order: {e}"