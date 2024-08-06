import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)''')
'''--------------------------------------------1 ДЗ--------------------------------------------'''
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', i*10, 1000))
#
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))
#
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}', ))
#
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> ?', (60, ))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

'''--------------------------------------------2 ДЗ--------------------------------------------'''
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
count_users = cursor.fetchone()[0]
print('Количество записей: ', count_users)

cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]
print('Сумма всех балансов: ', sum_balance)

print('Средний баланс: ', sum_balance/count_users)

connection.commit()
connection.close()