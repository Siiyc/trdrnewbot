import sqlite3

def init_db():
    conn = sqlite3.connect('alerts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT,
            side TEXT,
            cross TEXT,
            price REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_alert(token, side, cross, price):
    conn = sqlite3.connect('alerts.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO alerts (token, side, cross, price)
        VALUES (?, ?, ?, ?)
    ''', (token, side, cross, price))
    conn.commit()
    conn.close()

def get_alerts_by_token(token):
    conn = sqlite3.connect('alerts.db')
    c = conn.cursor()
    c.execute('''
        SELECT * FROM alerts WHERE token = ? ORDER BY timestamp ASC
    ''', (token,))
    rows = c.fetchall()
    conn.close()
    return rows
