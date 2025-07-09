import logging


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("binance_bot")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("bot.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


logger = setup_logger()
