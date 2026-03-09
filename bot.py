import requests
import time
import os

TOKEN = os.environ["BOT_TOKEN"]
SECOND_GROUP = -1002498229704

API = f"https://api.telegram.org/bot{TOKEN}"
offset = None

while True:
    r = requests.get(API + "/getUpdates", params={"offset": offset, "timeout": 30}).json()

    for upd in r.get("result", []):
        offset = upd["update_id"] + 1

        msg = upd.get("message")
        if not msg:
            continue

        if msg.get("text") == "/start sos":
            user = msg["from"]
            username = user.get("username")
            name = user.get("first_name", "")

            text = f"🚨 Сигнал от @{username}" if username else f"🚨 Сигнал от {name}"

            requests.post(API + "/sendMessage", json={
                "chat_id": SECOND_GROUP,
                "text": text
            })

            requests.post(API + "/sendMessage", json={
                "chat_id": msg["chat"]["id"],
                "text": "Сигнал отправлен"
            })

    time.sleep(1)
