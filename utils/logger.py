import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    heandler = logging.StreamHandler()
    heandler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    heandler.setFormatter(formatter)

    logger.addHandler(heandler)

    return logger

