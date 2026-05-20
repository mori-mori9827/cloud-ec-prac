from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id" : 1, "name" : "Keyboard", "price" : 8000},
    {"id" : 2, "name" : "Mouse", "price" : 3000},
    {"id" : 3, "name" : "Monitor", "price" : 24000},
]

@app.route("/")
def index():
  return "Cloud EC practice app is running!"

@app.route("/health")
def health():
  return jsonify({"status" : "OK"}), 200

@app.route("/items")
def get_items():
  return jsonify(items)

@app.route("/orders", methods=["POST"])
def create_order():
  data = request.get_json(silent=True) or {}
  return jsonify({
    "message": "order created",
    "order": data
  }), 201

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
