import json
from datetime import datetime

from logger import setup_logger

# Get logger
log_utils_logger = setup_logger("log_utils")


def log_api_request(request_obj, user_id=None):
    """
    Log detailed API request information

    Args:
        request_obj: Flask request object
        user_id (str, optional): User identifier if available
    """
    try:
        # Extract request data safely
        try:
            request_data = request_obj.get_json() if request_obj.is_json else {}
        except Exception:
            request_data = {}

        # For large payloads, truncate to avoid excessive logging
        if (
            request_data
            and isinstance(request_data, dict)
            and len(str(request_data)) > 1000
        ):
            request_data = {
                "message": f"Request data truncated (original size: {len(str(request_data))} chars)",
                "preview": str(request_data)[:500] + "...",
            }

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "request_id": getattr(request_obj, "request_id", "unknown"),
            "method": request_obj.method,
            "path": request_obj.path,
            "remote_addr": request_obj.remote_addr,
            "user_agent": request_obj.headers.get("User-Agent", "unknown"),
            "user_id": user_id,
            "content_type": request_obj.headers.get("Content-Type", "unknown"),
            "request_data": request_data,
            "query_params": dict(request_obj.args),
        }

        log_utils_logger.debug(f"API Request: {json.dumps(log_entry)}")
        return log_entry

    except Exception as e:
        log_utils_logger.error(f"Error logging API request: {str(e)}", exc_info=True)
        return None


def log_api_response(request_obj, response_obj, response_data=None, duration=None):
    """
    Log detailed API response information

    Args:
        request_obj: Flask request object
        response_obj: Flask response object
        response_data (dict, optional): Response data if available
        duration (float, optional): Request processing duration in seconds
    """
    try:
        # For large responses, truncate to avoid excessive logging
        if (
            response_data
            and isinstance(response_data, dict)
            and len(str(response_data)) > 1000
        ):
            response_data = {
                "message": f"Response data truncated (original size: {len(str(response_data))} chars)",
                "preview": str(response_data)[:500] + "...",
            }

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "request_id": getattr(request_obj, "request_id", "unknown"),
            "status_code": response_obj.status_code,
            "content_type": response_obj.headers.get("Content-Type", "unknown"),
            "duration": duration,
            "response_size": len(response_obj.get_data(as_text=True))
            if hasattr(response_obj, "get_data")
            else None,
            "response_data": response_data,
        }

        log_utils_logger.debug(f"API Response: {json.dumps(log_entry)}")
        return log_entry

    except Exception as e:
        log_utils_logger.error(f"Error logging API response: {str(e)}", exc_info=True)
        return None


def log_error(error, request_obj=None, context=None):
    """
    Log detailed error information

    Args:
        error: Exception object
        request_obj: Flask request object (optional)
        context (dict, optional): Additional context about the error
    """
    try:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "error_type": error.__class__.__name__,
            "error_message": str(error),
            "context": context or {},
        }

        if request_obj:
            log_entry["request_id"] = getattr(request_obj, "request_id", "unknown")
            log_entry["method"] = request_obj.method
            log_entry["path"] = request_obj.path

        log_utils_logger.error(
            f"Application Error: {json.dumps(log_entry)}", exc_info=True
        )
        return log_entry

    except Exception as e:
        log_utils_logger.error(f"Error logging error details: {str(e)}", exc_info=True)
        return None
