from flask import Flask, jsonify, request
from flask_cors import CORS
from logger import setup_logger

app = Flask(__name__)
CORS(app)

logger = setup_logger()


@app.route("/api/message", methods=["GET"])
def get_message():
    logger.info("Received GET request on /api/message")
    return jsonify({"message": "Hello from Flask!"})


@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    logger.info(f"Received POST request on /api/echo with data: {data}")
    return jsonify({"you_sent": data})


def leather_count(leather: str) -> int:
    counter = 0

    for i in range(len(leather)):
        if leather[i] != " ":
            counter += 1

        else:
            continue


if __name__ == "__main__":
    app.run(debug=True)
