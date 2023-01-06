import logging


def create_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(f"logs/{name}.log")
    formatter = logging.Formatter(f"[%(levelname)s]: [%(name)s] %(asctime)s:\n"
                                  f"%(message)s", datefmt='%d.%m.%y %H:%M:%S')

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
