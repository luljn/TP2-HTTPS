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
    
    query_1 = "INSERT INTO users (email, password) VALUES (\"mbohlula@gmail.com\", \"748713b28662fec78cac7cdb31e76f0ce8cc1902837e4d15e5564bcc3fe99da7\");"
    cursor.execute(query_1)
    
    conn.commit()
    conn.close()

initDatabase()