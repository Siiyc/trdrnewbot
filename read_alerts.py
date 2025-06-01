from db import get_alerts_by_token

token = "SOLUSDT"  # можно поменять на любой нужный токен
alerts = get_alerts_by_token(token)

for alert in alerts:
    print(alert)
