from src.log_utils import log_error
from src.logger import setup_logger

logger = setup_logger("example_script")


def main():
    logger.info("Example script started")

    # Log different levels
    logger.debug("This is a debug message - only visible with LOG_LEVEL=DEBUG")
    logger.info("This is an info message")
    logger.warning("This is a warning message")

    # Example of handling and logging errors
    try:
        # Deliberately cause an error for demonstration
        value = 0
        logger.info(f"Attempting to divide 100 by {value}")
        result = 100 / value  # This will cause a ZeroDivisionError
        logger.info(f"Result: {result}")  # This line will not execute
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        log_error(e, context={"operation": "division", "value": 0})
        # Comment out the next line to see the difference - exception will propagate
        # return  # Exit the function, preventing "script completed" message

    logger.info(
        "Example script completed"
    )  # This will still execute with the try/except


def proper_error_handling():
    """This function demonstrates proper error handling that prevents execution from continuing."""
    logger.info("Starting proper_error_handling function")

    try:
        logger.info("Attempting another division by zero")
        result = 200 / 0
        return result  # This line won't execute
    except Exception as e:
        logger.error(f"Proper error handling caught: {str(e)}")
        log_error(e, context={"function": "proper_error_handling"})
        return None  # Return a value to indicate failure
    finally:
        # The finally block always executes
        logger.info("Finally block in proper_error_handling")

    # This line won't execute if an exception occurs
    logger.info("This message will never be seen if an error occurs")


if __name__ == "__main__":
    main()

    # Try the proper error handling function
    logger.info("---")
    logger.info("Now trying proper error handling function")
    result = proper_error_handling()

    # This will only execute if proper_error_handling doesn't raise an uncaught exception
    if result is None:
        logger.warning("proper_error_handling function encountered an error")
    else:
        logger.info(f"proper_error_handling function succeeded with result: {result}")

    logger.info("Script finished completely")
