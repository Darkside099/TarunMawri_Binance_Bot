from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from logger import logger
from utils import validate_symbol, validate_order_side, validate_quantity


def place_oco_order(symbol: str, side: str, quantity: str, tp_price: str, sl_price: str):
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)

    try:
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="TAKE_PROFIT_MARKET",
            stopPrice=str(tp_price),
            closePosition=False,
            quantity=float(quantity),
            timeInForce="GTC"
        )

        sl_order = client.futures_create_order(
            symbol=symbol,
            side="SELL" if side.upper() == "BUY" else "BUY",
            type="STOP_MARKET",
            stopPrice=str(sl_price),
            closePosition=False,
            quantity=float(quantity),
            timeInForce="GTC"
        )

        logger.info(f"OCO TP/SL Orders placed: TP: {tp_order}, SL: {sl_order}")
        return {"take_profit": tp_order, "stop_loss": sl_order}

    except Exception as e:
        logger.error(f"OCO order error: {e}")
        return f"Error placing OCO orders: {e}"