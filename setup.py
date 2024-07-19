import sqlite3
from  text_file_reset import reset_text_files
import hashlib
from datetime import datetime
import os
from user_table_fun import make_users_table_name



conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

time = datetime.now()
date_now = time.date()
time_now = time.time()

# main table where they will keep all user info
cursor.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER, name TEXT, password TEXT, dob DATETIME, amount INTEGER,  email TEXT NOT NULL UNIQUE, account_creating_date DATETIME , account_creating_time DATETIME , last_login DATETIME , PRIMARY KEY(id AUTOINCREMENT))")
conn.commit()

# Creating Admin Access.

cursor.execute("SELECT * FROM customer WHERE id = 1")
data_admin = cursor.fetchone()

if data_admin == None:
    print("\nAdmin Account Creating....So be CAREFUL...\n ")
    print("Name: Admin")
    dob = input("Date of birth (YYYY-MM-DD): ")
    amount = input("The amount of money you want to keep in the bank: ")
    email = input("Email Address: ")
    plain_password  = input("Type your password: ")
    plain_password_again  = input("Type your password again: ")

    if plain_password != plain_password_again:
        print("Password Didn't Matched.")
        print("Admin Access Creating Failed.\n Re-run the setup.py")
        
        os.remove("bank.db")
        exit()

    else:
        password = hashlib.sha256(plain_password.encode()).hexdigest()
        cursor.execute("INSERT INTO customer (id,name,password,dob,amount,account_creating_date,account_creating_time,email,last_login) VALUES(?,?,?,?,?,?,?,?,?)", (1,"Admin", password, dob, amount, date_now.strftime("%Y-%m-%d") , time_now.strftime("%H:%M:%S") , email, time.strftime("%Y-%m-%d %H:%M:%S"),))
        conn.commit()
        make_users_table_name("Admin",1)
        print("Admin Account Created Sucessfully.\nName: Admin\nId:1")

else:
    print("Admin Account Was Created.")

# Done creating Admin Access. 


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
conn.commit()


conn.close()
reset_text_files()


print("Your setup is done.")