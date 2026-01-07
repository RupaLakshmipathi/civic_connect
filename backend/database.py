import sqlite3

def init_db():
    conn = sqlite3.connect('civics.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            category TEXT,
            priority TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_issue(description, category, priority):
    conn = sqlite3.connect('civics.db')
    c = conn.cursor()
    c.execute("INSERT INTO issues VALUES (NULL, ?, ?, ?)",
              (description, category, priority))
    conn.commit()
    conn.close()

def get_all_issues():
    conn = sqlite3.connect('civics.db')
    c = conn.cursor()
    c.execute("SELECT * FROM issues")
    data = c.fetchall()
    conn.close()
    return data
