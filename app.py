from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    name = data.get("name", "мир")
    return jsonify({"result": f"Привет, {name}!"})
