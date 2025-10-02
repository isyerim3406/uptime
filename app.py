from flask import Flask, send_file
import io
import os

app = Flask(__name__)

# Ana sayfa
@app.route("/")
def home():
    return "App is alive!"

# Boş favicon.ico route'u (404 engelleme)
@app.route("/favicon.ico")
def favicon():
    empty_icon = io.BytesIO(b'\x00\x00\x00\x00')
    return send_file(empty_icon, mimetype='image/x-icon')

if __name__ == "__main__":
    # Render'den gelen port değişkeni
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
