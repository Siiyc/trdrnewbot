import requests

BOT_TOKEN = "7791732364:AAHzYIPNJNMDW8m1wRWkJhjIx6cVz06iWag"

def get_updates():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    print(response.json())

get_updates()