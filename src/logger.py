import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

from src.config import LOG_CONFIG, get_log_level

# Define log directory path
LOG_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "log"
)

# Ensure log directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


# Create logger
def setup_logger(name="flask_api", log_level=None):
    """
    Set up and configure a logger instance

    Args:
        name (str): Name of the logger
        log_level (int, optional): Logging level (default: from config)

    Returns:
        logging.Logger: Configured logger instance
    """
    # Use configured log level if not specified
    if log_level is None:
        log_level = get_log_level()

    # Create logger instance
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Create file handler for logging to file
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(LOG_DIR, f"api_{today}.log")
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=LOG_CONFIG["MAX_LOG_SIZE"],
            backupCount=LOG_CONFIG["BACKUP_COUNT"],
        )
        file_handler.setLevel(log_level)

        # Create console handler for logging to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter(
            LOG_CONFIG["LOG_FORMAT"], datefmt=LOG_CONFIG["DATE_FORMAT"]
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
