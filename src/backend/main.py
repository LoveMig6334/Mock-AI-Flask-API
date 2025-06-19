from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from React (CORS policy)


@app.route("/api/message", methods=["GET"])
def get_message():
    return jsonify({"message": "Hello from Flask!"})


@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data})


if __name__ == "__main__":
    app.run(debug=True)
