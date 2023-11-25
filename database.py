import sqlite3

connect = sqlite3.connect("app.db")
print("Connection is successful!")

connect.execute(
    "CREATE TABLE app_test(question TEXT, ans TEXT, correction TEXT)"
)
print("Table is created successful!")
connect.close()
