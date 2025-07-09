import time
from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from logger import logger
from utils import validate_symbol, validate_order_side, validate_quantity


def place_twap_order(symbol: str, side: str, total_qty: str, chunks: int = 5, delay: int = 5):
    if not all([
        validate_symbol(symbol),
        validate_order_side(side),
        validate_quantity(total_qty)
    ]):
        logger.error(f"Invalid TWAP input: {symbol}, {side}, {total_qty}")
        return "Invalid input"

    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)

    try:
        chunk_qty = float(total_qty) / chunks
        responses = []

        for i in range(chunks):
            logger.info(f"TWAP Chunk {i + 1}: placing market order of {chunk_qty} {symbol}")
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=round(chunk_qty, 3)
            )
            logger.info(f"Chunk {i + 1} executed: {order}")
            responses.append(f"Chunk {i + 1} executed: {order['orderId']}")
            time.sleep(delay)

        logger.info("TWAP completed")
        return "\n".join(responses + ["TWAP completed"])

    except Exception as e:
        logger.error(f"TWAP error: {e}")
        return f"Error executing TWAP: {e}"