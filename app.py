import os
import requests
from flask import Flask
from threading import Thread
import time

app = Flask(__name__)

# UptimeRobot URL’i
UPTIMEROBOT_URL = os.environ.get("UPTIMEROBOT_URL")

@app.route("/")
def home():
    return "Alive!"

def ping_uptimerobot():
    while True:
        if UPTIMEROBOT_URL:
            try:
                r = requests.get(UPTIMEROBOT_URL, timeout=10)
                if r.status_code == 200:
                    print("✅ Ping successful")
                else:
                    print(f"⚠ Ping failed with status {r.status_code}")
            except Exception as e:
                print(f"❌ Ping error: {e}")
        time.sleep(300)  # 5 dakika bekle

# Thread başlat
Thread(target=ping_uptimerobot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
