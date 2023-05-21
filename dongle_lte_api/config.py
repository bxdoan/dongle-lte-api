import logging


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel("DEBUG")

    # Create handlers
    c_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    # Configure the logger
    simple_format = logging.Formatter(
        "%(asctime)s [%(funcName)s() +%(lineno)d]: %(levelname)-8s %(message)s",
        datefmt="%b-%d %H:%M:%S%Z"
    )
    c_handler.setFormatter(simple_format)

    # Add handlers to the logger
    log.addHandler(c_handler)

    return log


# Use this variable for global project
logger = get_logger(__name__)
