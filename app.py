from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Basit listeyle logları saklayacağız
ping_logs = []

@app.route("/")
def index():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    ping_logs.append(now)
    print(f"[PING] {now}")  # Render loglarında gözükecek
    # Sadece son 10 ping’i gösterelim
    last_pings = "<br>".join(ping_logs[-10:])
    return f"<h3>UptimeRobot Ping Logs (last 10)</h3><p>{last_pings}</p>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
