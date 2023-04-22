from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hi"


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()