import os
from urllib.parse import unquote_plus
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def greet():
    name_raw = request.args.get("name", "Stranger")
    msg_raw  = request.args.get("message", "")
    name = unquote_plus(name_raw)
    message = unquote_plus(msg_raw)
    return f"Hello {name}! {message}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
