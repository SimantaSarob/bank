import sqlite3
from datetime import datetime
from time import strftime
from id_num_fun import id_num
from user_table_fun import make_users_table_name
from login_fun import login

####################################
#                                  #
#   full logic in main.py file.    #
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
    
    cursor.execute("INSERT INTO customer (name,password,dob,amount,account_creating_date,account_creating_time,email) VALUES(?,?,?,?,?,?,?)", ( name_sql , password_sql , dob_sql , amount_sql , date_now.strftime("%Y-%m-%d") , time_now.strftime("%H:%M:%S") , email_sql ,))
    conn.commit()
    conn.close()
    showing_data_for_login(name,password,email)  #sending our data showing_data_for_login function to show the users to remember data for login.
    

def showing_data_for_login(name, password, email):
    
    # Never use this function anywhere else
    
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM customer WHERE name = ? AND email = ?",(name,email,))
    id_num = cursor.fetchone()
    conn.commit()
    conn.close()
    
    text = f'''
    ----------------------------------------------------------------------------------
    #   YOU NEED TO REMEMBER THIS DATA:
    #
    #   NAME     : {name}
    #   ID       : {id_num[0]}
    #   PASSWORD : you know that.
    #   
    #   this data will help you to interact with your account.
    ----------------------------------------------------------------------------------
    '''
    print(text)
    
    login(name, password, id = str(id_num[0]))
    make_users_table_name(name, id = int(id_num[0]))
    
    