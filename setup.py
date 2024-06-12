import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER, name TEXT, password TEXT, dob DATETIME, amount INTEGER,  email TEXT NOT NULL UNIQUE, account_creating_date DATETIME , account_creating_time	DATETIME , PRIMARY KEY(id AUTOINCREMENT))")
conn.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS history (command_number INTEGER PRIMARY KEY AUTOINCREMENT,id INTEGER, name TEXT, command TEXT, execution_time NUMERIC)")
conn.commit()

conn.close()

file_name = open("name.txt",'w')
file_password = open("password.txt", 'w')
file_id = open("id.txt", "w")
file_user_table = open("loged-in_users_table_name.txt",'w')
file_user_table.write("default")
file_status = open("status.txt", 'w')
file_status.write("loged out")

print("setup done.")