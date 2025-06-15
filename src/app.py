# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # เปิดให้ Next.js frontend เข้าถึงได้


# ตัวอย่างจำลอง LLM ขนาดเล็ก (mock)
def small_llm(prompt):
    return f"AI: ฉันได้รับข้อความว่า '{prompt}' แล้วนะ!"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    # ประมวลผลข้อความผ่าน LLM จำลอง
    response = small_llm(user_input)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(port=5000)
