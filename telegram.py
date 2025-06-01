import requests

BOT_TOKEN = "7791732364:AAHzYIPNJNMDW8m1wRWkJhjIx6cVz06iWag"
CHAT_ID = 84360339

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print("❌ Ошибка отправки в Telegram:", response.text)
    except Exception as e:
        print("❌ Исключение при отправке в Telegram:", e)