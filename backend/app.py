from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Allow the Node/Express frontend (running on a different origin/port) to call this API
CORS(app)


@app.route("/")
def helloworld():
    return jsonify({"status": "ok", "message": "Flask backend is running."})


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name:
        return jsonify({"error": "Name is required."}), 400

    reply = f"Hello {name}! Your submission was received successfully."
    return jsonify({
        "message": reply,
        "received": {
            "name": name,
            "email": email,
            "message": message,
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
