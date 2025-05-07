import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            phone TEXT UNIQUE,
            name TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_user(phone, name, email):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (phone, name, email) VALUES (?, ?, ?)", (phone, name, email))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def get_user_name(phone):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT name FROM users WHERE phone=?", (phone,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None
# This code initializes a SQLite database, creates a table for users, and provides functions to save and retrieve user information.
# The `init_db` function creates the database and table if they don't exist, while `save_user` inserts a new user or ignores duplicates.
# The `get_user_name` function retrieves the name associated with a given phone number.
# This code is useful for managing user data in a simple application, such as a phone number identifier.
# The database is stored in a file named 'data.db', and the table is named 'users'.
# The table has columns for user ID, phone number, name, and email.
# The `save_user` function uses a try-except block to handle unique constraint violations, ensuring that duplicate phone numbers are ignored.