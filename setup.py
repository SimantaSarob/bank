import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER, name TEXT, password TEXT, dob DATETIME, amount INTEGER, account_creating_date DATETIME DEFAULT 'none', account_creating_time	DATETIME DEFAULT 'none', PRIMARY KEY(id AUTOINCREMENT))")
conn.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS history (command_number INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, command TEXT, execution_time NUMERIC)")
conn.commit()

conn.close()

file_name = open("name.txt",'w')
file_password = open("password.txt", 'w')
file_id = open("id.txt", "w")

print("setup done.")