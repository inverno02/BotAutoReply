from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Lark Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    # Cek apakah ada event message
    if "event" in data and data["event"]["type"] == "message":
        chat_id = data["event"]["message"]["chat_id"]
        
        # Kirim balasan otomatis
        response = {
            "chat_id": chat_id,
            "msg_type": "text",
            "content": '{"text": "maaf, lama merespon. Untuk sementara bisa bertanya kepada SmartHR untuk pertanyaan anda."}'
        }
        return jsonify(response)
    
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)
