import time
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

from log_utils import log_api_request, log_api_response, log_error
from logger import setup_logger

# Initialize logger
logger = setup_logger()

app = Flask(__name__)
CORS(app)


# Request logging middleware
@app.before_request
def log_request_info():
    # Generate unique request ID
    request.request_id = str(uuid.uuid4())

    # Log request details
    logger.info(
        f"Request ID: {request.request_id} | Method: {request.method} | Path: {request.path}"
    )

    # Store start time for response timing
    request.start_time = time.time()

    # Log detailed request information
    log_api_request(request)


@app.after_request
def log_response_info(response):
    # Calculate request processing time
    duration = time.time() - request.start_time

    # Log response details
    logger.info(
        f"Request ID: {request.request_id} | "
        f"Status: {response.status_code} | "
        f"Duration: {duration:.4f}s"
    )
    # Log detailed response information
    try:
        response_data = None
        if response.is_json:
            response_data = response.get_json()
    except Exception as e:
        logger.warning(f"Could not parse JSON response: {str(e)}")
        response_data = None

    log_api_response(request, response, response_data, duration)

    return response


def small_llm(prompt):
    logger.debug(f"LLM input: {prompt}")
    response = f"AI: ฉันได้รับข้อความว่า '{prompt}' แล้วนะ!"
    logger.debug(f"LLM output: {response}")
    return response


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        logger.info(f"Chat request received with message: {user_input}")

        response = small_llm(user_input)

        logger.info("Chat response generated successfully")

        return jsonify({"response": response, "request_id": request.request_id})

    except Exception as e:
        # Log error with detailed context
        error_context = {
            "message_input": user_input if "user_input" in locals() else "Not available"
        }
        log_error(e, request, error_context)

        # Return error response
        return jsonify(
            {
                "error": "Internal server error",
                "request_id": getattr(request, "request_id", "unknown"),
            }
        ), 500


if __name__ == "__main__":
    logger.info("Starting Flask API server on port 5000")
    app.run(port=5000)
