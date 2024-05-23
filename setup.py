import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT, dob DATE, amount TEXT);")
conn.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS history (command_number INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, command TEXT, execution_time NUMERIC)")

conn.commit()
conn.close()

file_name = open("name.txt",'w')
file_name.write('')
file_password = open("password.txt", 'w')
file_password.write
print("setup done.")