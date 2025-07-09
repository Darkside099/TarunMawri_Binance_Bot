def validate_symbol(symbol: str) -> bool:
    return symbol.endswith("USDT")


def validate_order_side(side: str) -> bool:
    return side.upper() in ["BUY", "SELL"]


def validate_quantity(qty: str) -> bool:
    try:
        return float(qty) > 0
    except ValueError:
        return False
