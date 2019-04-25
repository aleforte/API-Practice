import sqlite3

conn = sqlite3.connect('database.db')
print("Opened Database successfully!")

conn.execute("""CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER)""")

print("Table Created Successfully")
conn.close()
