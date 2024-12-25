# Код из предыдущего задания
import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# for i in range(10):
#     cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example1{i}@gmail.com", str(random.randint(18,49)), random.randint(100,5000)))
# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f'User{i}'))
# for i in range(0, 10, 3):
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f'User{i}',))
cursor.execute("SELECT username, age FROM Users WHERE age > ?", (40,))
users = cursor.fetchall()
for user in users:
    print(user)

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchall()[0]
print(total_users)

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances  = cursor.fetchall()[0]
print(all_balances )

# средний баланс всех пользователей
print(all_balances / total_users)

connection.commit()
connection.close()


