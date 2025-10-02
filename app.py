import os
from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

# -----------------------------
# Alive route (UptimeRobot ping atacak)
# -----------------------------
@app.route("/")
def home():
    return "Bot is alive!", 200

# -----------------------------
# Örnek bot fonksiyonu
# -----------------------------
def bot_loop():
    while True:
        # Buraya botun yapmasını istediğin işlemleri ekle
        print("Bot is running...")
        time.sleep(60)  # 1 dakikada bir çalışıyor

# -----------------------------
# Opsiyonel self ping (test)
# -----------------------------
def self_ping():
    url = os.environ.get("SELF_PING_URL")  # .env veya Render env variable
    if not url:
        return
    while True:
        try:
            requests.get(url)
            print(f"Pinged {url}")
        except Exception as e:
            print(f"Ping error: {e}")
        time.sleep(300)  # 5 dakikada bir ping

# -----------------------------
# Thread başlat
# -----------------------------
threading.Thread(target=bot_loop, daemon=True).start()
threading.Thread(target=self_ping, daemon=True).start()

# -----------------------------
# Flask app başlat
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render PORT kullanır
    app.run(host="0.0.0.0", port=port)
