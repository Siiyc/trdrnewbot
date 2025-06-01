from flask import Flask, request
from db import init_db, insert_alert
from logic import should_notify
from telegram import send_telegram_message

app = Flask(__name__)

# Инициализация базы при старте
init_db()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🚨 Получен сигнал:")
    print(data)

    content = data.get("content", "")
    try:
        # Пример: side=short token=AVAXUSDT cross=1/2.5 price=21.02
        parts = content.strip().split()
        parsed = {kv.split("=")[0]: kv.split("=")[1] for kv in parts}
        side = parsed["side"]
        token = parsed["token"]
        cross = parsed["cross"].replace("/", "")  # 1/2.5 → 1k2t5 формат
        price = float(parsed["price"])
    except Exception as e:
        print("❌ Ошибка разбора строки:", e)
        return '', 400

    # Объект сигнала
    parsed_alert = {
        "side": side.lower(),
        "token": token.upper(),
        "cross": cross.lower(),
        "price": price
    }

    # Обработка
    notify = should_notify(parsed_alert)
    if notify:
        print("📢 Уведомление: отправка пользователю")
        symbol = "🟢" if side.lower() == "long" else "⭕️"
        pretty = f"{symbol}#{token}{cross}  цена #{token[:-4]}/{token[-4:]}  {price}"
        send_telegram_message(pretty)
        insert_alert(token, side, cross, price)
    else:
        print("⛔ Пропуск: условия не выполнены")

    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
