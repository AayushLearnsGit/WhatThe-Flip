import sqlite3

def connect():
    conn = sqlite3.connect('./under_tracking')
    query = '''CREATE TABLE IF NOT EXISTS tracking (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price FLOAT, url TEXT)'''
    conn.execute(query)
    return conn


if __name__ == '__main__':
    connect()