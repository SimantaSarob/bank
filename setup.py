import sqlite3
from  text_file_reset import reset_text_files
    

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


# main table where they will keep all user info
cursor.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER, name TEXT, password TEXT, dob DATETIME, amount INTEGER,  email TEXT NOT NULL UNIQUE, account_creating_date DATETIME , account_creating_time	DATETIME , PRIMARY KEY(id AUTOINCREMENT))")
conn.commit()


# will keep every command's history of every user's
cursor.execute("CREATE TABLE IF NOT EXISTS history (event_no INTEGER PRIMARY KEY AUTOINCREMENT,id INTEGER, name TEXT, command TEXT, execution_time NUMERIC)")
conn.commit()


# will keep every deposite command from every user
cursor.execute("CREATE TABLE IF NOT EXISTS deposite_history (event_no INTEGER PRIMARY KEY AUTOINCREMENT , date DATETIME , time DATETIME , id INTEGER , name TEXT , amount INTEGER , deposite_amount INTEGER , new_amount INTEGR )")
conn.commit()


# will keep every withdrew command from every user
cursor.execute("CREATE TABLE IF NOT EXISTS withdrew_history (event_no INTEGER PRIMARY KEY AUTOINCREMENT , date DATETIME , time DATETIME , id INTEGER , name TEXT , amount INTEGER , withdrew_amount INTEGER , new_amount INTEGR )")
conn.commit()


# will keep every send money command from every user
cursor.execute("CREATE TABLE IF NOT EXISTS send_money_history (event_no INTEGER PRIMARY KEY AUTOINCREMENT , date DATETIME , time DATETIME , id INTEGER , name TEXT , amount INTEGER , receiver_amount INTEGER , receiver_id INTEGER , receiver_name TEXTS , new_amount INTEGR )")


conn.close()

reset_text_files()

print("Your setup is done.")