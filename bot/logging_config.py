import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    log_dir = "./logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "trading_bot.log")

    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    # File handler
    file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
    file_handler.setLevel(logging.DEBUG)

    # Use a clean summary representation format for logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Only add handler if not already present
    if not logger.handlers:
        logger.addHandler(file_handler)
        
    return logger

logger = setup_logger()
