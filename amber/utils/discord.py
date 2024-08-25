import os, requests, threading

def notify(msg: str):
    requests.post(
        os.getenv("DISCORD_WEBHOOK"),
        json={
            "content": msg,
        }
    )

def notify_background(msg: str):
    thread = threading.Thread(target=notify, args=(msg,))
    thread.start()
