import requests, threading

def notify(msg: str):
    requests.post(
        "https://discord.com/api/webhooks/1276865274397855816/og2wkWfVKzeaLjrAxPP8XTu_un7hXx3whzBbdNNManNLaI5Hw-WVwZbzWh7NRRerhebE",
        json={
            "content": msg,
        }
    )

def notify_background(msg: str):
    thread = threading.Thread(target=notify, args=(msg,))
    thread.start()
