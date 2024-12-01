import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email NEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User1", "example1@gmail.com", "10", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User2", "example2@gmail.com", "20", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User3", "example3@gmail.com", "30", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User4", "example4@gmail.com", "40", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User5", "example5@gmail.com", "50", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User6", "example6@gmail.com", "60", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User7", "example7@gmail.com", "70", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User8", "example8@gmail.com", "80", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User9", "example9@gmail.com", "90", "1000"))
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User10", "example10@gmail.com", "100", "1000"))
#
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, 'User1'))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, 'User3'))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, 'User5'))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, 'User7'))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, 'User9'))
#
# cursor.execute("DELETE FROM Users WHERE username = ?", ("User1",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("User4",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("User7",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("User10",))

# cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(user)

# ------------------------------module 14.2 ----------------------------------

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close