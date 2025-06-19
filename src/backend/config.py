# Configuration options for the logging system
import logging
import os

# Base configuration
LOG_CONFIG = {
    # Log level - can be DEBUG, INFO, WARNING, ERROR, CRITICAL
    "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
    # Max log file size before rotation (in bytes)
    "MAX_LOG_SIZE": int(os.environ.get("MAX_LOG_SIZE", 10485760)),  # 10MB
    # Number of backup log files to keep
    "BACKUP_COUNT": int(os.environ.get("BACKUP_COUNT", 10)),
    # Whether to include stack traces in error logs
    "INCLUDE_STACK_TRACE": os.environ.get("INCLUDE_STACK_TRACE", "True").lower()
    == "true",
    # Whether to log detailed request and response data
    "LOG_DETAILED_REQUESTS": os.environ.get("LOG_DETAILED_REQUESTS", "True").lower()
    == "true",
    # Format for log messages
    "LOG_FORMAT": os.environ.get(
        "LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ),
    # Date format for log messages
    "DATE_FORMAT": os.environ.get("DATE_FORMAT", "%Y-%m-%d %H:%M:%S"),
}

# Log level mapping
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


# Get log level from config
def get_log_level():
    level = LOG_CONFIG["LOG_LEVEL"].upper()
    return LOG_LEVELS.get(level, logging.INFO)
