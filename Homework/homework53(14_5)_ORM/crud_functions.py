def initiate_db(connection, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )''')
    connection.commit()

def get_all_products(cursor):
    cursor.execute('SELECT title, description, price FROM Products')
    return cursor.fetchall()

def add_user(cursor, connection, username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))
    connection.commit()

def is_included(cursor, username):
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username == ?', (username,))
    return bool(cursor.fetchone()[0])