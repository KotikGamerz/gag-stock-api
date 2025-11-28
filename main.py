from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Grow A Garden API is running!"

@app.route("/stock")
def stock():
    return jsonify({
        "seeds": [
            "Watermelon x5",
            "Tomato x1",
            "Blueberry x2",
            "Strawberry x3"
        ],
        "gear": [
            "Basic Sprinkler x3",
            "Wrench x1"
        ],
        "eggs": [
            "Uncommon Egg x1",
            "Rare Egg x1",
            "Epic Egg x1"
        ]
    })

if __name__ == "__main__":
    # Very important for Render
    app.run(host="0.0.0.0", port=10000)
