import sqlite3

connection = sqlite3.connect("app.db")
print("Database is created successfully")


connection.execute(
    """
    CREATE TABLE test (question TEXT, answer TEXT, answer2 TEXT, correction TEXT)
    """
)
print("Table is created successfully")
connection.close()
