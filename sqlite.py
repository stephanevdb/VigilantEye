import sqlite3

def dbinit():
    db = sqlite3.connect('database.db',check_same_thread=False)
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workers(
            id TEXT PRIMARY KEY,
            online INTEGER DEFAULT 0,
            ipv4_capable INTEGER,
            ipv4_address TEXT,
            ipv6_capable INTEGER,
            ipv6_address TEXT,
            worker_ip TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            worker_id TEXT,
            output TEXT, 
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()

def execute(query, args=()):
    db = sqlite3.connect('database.db',check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(query, args)
    db.commit()
    return cursor