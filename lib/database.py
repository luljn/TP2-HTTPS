import sqlite3


def initDatabase():
    conn = sqlite3.connect('lib/database.sql')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    ''')
    
    query_1 = "INSERT INTO users (email, password) VALUES (\"mbohlula@gmail.com\", \"aa9c7c8c5992ee282a0962b072085048\");"
    cursor.execute(query_1)
    
    conn.commit()
    conn.close()

initDatabase()