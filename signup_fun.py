import sqlite3
from datetime import datetime
from time import strftime

####################################
#                                  #
#   full loggic in main.py file.   #
#                                  #
####################################

def signup(name, password, dob, amount, email):
    name_sql = name
    password_sql = password
    dob_sql = dob
    amount_sql = float(amount)
    email_sql = email
    
    time = datetime.now()
    date_now = time.date()
    time_now = time.time()
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO customer (name,password,dob,amount,account_creating_date,account_creating_time,email) VALUES(?,?,?,?,?,?)",(name_sql,password_sql, dob_sql, amount_sql, date_now.strftime("%Y-%m-%d"),time_now.strftime("%H:%M:%S"),email_sql))
    
    conn.commit()
    conn.close()
    
    print("ok. done.")