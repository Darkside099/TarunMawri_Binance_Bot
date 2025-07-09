from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from logger import logger
from utils import validate_symbol, validate_order_side, validate_quantity


def place_stop_limit_order(symbol: str, side: str, quantity: str, stop_price: str, limit_price: str):
    if not all([
        validate_symbol(symbol),
        validate_order_side(side),
        validate_quantity(quantity)
    ]):
        logger.error(f"Invalid input: {symbol}, {side}, {quantity}, {stop_price}, {limit_price}")
        return "Invalid input"

    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)

    try:
        current_price = float(client.futures_symbol_ticker(symbol=symbol)["price"])
        stop_price = float(stop_price)
        if side.upper() == "BUY" and stop_price <= current_price:
            return f"Invalid stop price: must be GREATER than current market price ({current_price}) for BUY orders."
        elif side.upper() == "SELL" and stop_price >= current_price:
            return f"Invalid stop price: must be LOWER than current market price ({current_price}) for SELL orders."
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP_MARKET",
            stopPrice=str(stop_price),
            closePosition=False,
            timeInForce="GTC",
            quantity=float(quantity),
            workingType="MARK_PRICE"
        )
        logger.info(f"Stop-Limit order placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Stop-Limit order error: {e}")
        return f"Error placing stop-limit order: {e}"
