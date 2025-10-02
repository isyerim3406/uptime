from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    # Ping geldiğini logla
    print(f"[PING] {now} - {request.remote_addr}")
    return "Alive", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render default portu kullan
