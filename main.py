from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/stock")
def stock():
    return jsonify({
        "seeds": [
            "Watermelon x5",
            "Tomato x1",
            "Blueberry x2"
        ],
        "gear": [
            "Basic Sprinkler x3",
            "Wrench x1"
        ],
        "eggs": [
            "Uncommon Egg x1",
            "Rare Egg x1"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
