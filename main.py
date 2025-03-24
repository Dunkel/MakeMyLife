from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Привет от Кощей API!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
