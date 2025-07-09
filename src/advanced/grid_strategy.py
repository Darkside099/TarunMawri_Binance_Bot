from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from logger import logger


def place_grid_orders(symbol: str, base_price: float, grid_size: int, gap_percent: float, qty: float):
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)

    try:
        base = float(base_price)
        gap = float(gap_percent) / 100
        quantity = float(qty)

        for i in range(1, grid_size + 1):
            buy_price = base * (1 - gap * i)
            sell_price = base * (1 + gap * i)

            client.futures_create_order(
                symbol=symbol,
                side="BUY",
                type="LIMIT",
                quantity=quantity,
                price=str(round(buy_price, 2)),
                timeInForce="GTC"
            )

            client.futures_create_order(
                symbol=symbol,
                side="SELL",
                type="LIMIT",
                quantity=quantity,
                price=str(round(sell_price, 2)),
                timeInForce="GTC"
            )

            logger.info(f"Grid {i}: Buy @ {buy_price}, Sell @ {sell_price}")

        return f"Placed {grid_size * 2} grid orders"
    except Exception as e:
        logger.error(f"Grid strategy error: {e}")
        return f"Error in grid strategy: {e}"
