from db import get_alerts_by_token

def should_notify(new_alert):
    side = new_alert["side"]
    token = new_alert["token"]
    cross = new_alert["cross"]
    price = float(new_alert["price"])

    # Получаем все прошлые сигналы по этому токену
    previous_alerts = get_alerts_by_token(token)
    if not previous_alerts:
        return True  # первый сигнал по токену — отправляем

    # Последний сигнал по токену
    last_alert = previous_alerts[-1]
    last_side = last_alert[2]  # поле 'side'

    if last_side != side:
        return True  # смена направления — отправляем

    # Та же сторона (лонг или шорт)
    # Смотрим, был ли такой же кросс ранее с этой стороной
    same_cross_alert = None
    for alert in reversed(previous_alerts):
        if alert[2] == side and alert[3] == cross:
            same_cross_alert = alert
            break

    if same_cross_alert:
        previous_price = float(same_cross_alert[4])
        if side == "long":
            return price < previous_price * 0.99
        elif side == "short":
            return price > previous_price * 1.01
        else:
            return False  # непонятная сторона
    else:
        return True  # такого кросса не было ранее — отправляем
