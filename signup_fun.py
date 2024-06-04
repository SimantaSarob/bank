import sqlite3
from datetime import datetime
from time import strftime


def signup(name, password, dob, amount):
    name_sql = name
    password_sql = password
    dob_sql = dob
    amount_sql = float(amount)
    
    time = datetime.now()
    date_now = time.date()
    time_now = time.time()
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO customer (name,password,dob,amount,account_creating_date,account_creating_time) VALUES(?,?,?,?,?,?)",(name_sql,password_sql, dob_sql, amount_sql, date_now.strftime("%Y-%m-%d"),time_now.strftime("%H:%M:%S"),))
    conn.commit()
    conn.close()
    
    print("ok. done.")