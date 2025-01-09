import logging
import os
import json
from logging.handlers import RotatingFileHandler



def setup_logger(service_name, log_dir='logs', log_level=logging.INFO):
    """
    Sets up a logger with a rotating file handler.

    :param service_name: Name of the service (e.g., 'api', 'cli')
    :param log_dir: Directory where log files will be stored
    :param log_level: Logging level
    :return: Configured logger
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{service_name}.log")

    logger = logging.getLogger(service_name)
    logger.setLevel(log_level)

    handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5)
    handler.setLevel(log_level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
