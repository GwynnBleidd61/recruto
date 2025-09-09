from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def greet():
    name = request.args.get("name", "Stranger")
    message = request.args.get("message", "")
    return f"Hello {name}! {message}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
