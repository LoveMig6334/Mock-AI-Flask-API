# Example script showing how to use the logging system
import os
import sys

from src.log_utils import log_error
from src.logger import setup_logger

# Add parent directory to sys.path to allow importing from src
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

# Set up logger
logger = setup_logger("example_script")


def main():
    logger.info("Example script started")

    # Log different levels
    logger.debug("This is a debug message - only visible with LOG_LEVEL=DEBUG")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    # Example of handling and logging errors
    try:
        # Deliberately cause an error
        _ = 100 / 0  # using _ to indicate we don't care about the result
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        log_error(e, context={"operation": "division", "value": 0})

    logger.info("Example script completed")


if __name__ == "__main__":
    main()
