import select
import sqlite3
from datetime import datetime
from time import strftime
from token import NAME

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
    
    cursor.execute("INSERT INTO customer (name,password,dob,amount,account_creating_date,account_creating_time,email) VALUES(?,?,?,?,?,?,?)", ( name_sql , password_sql , dob_sql , amount_sql , date_now.strftime("%Y-%m-%d") , time_now.strftime("%H:%M:%S") , email_sql ,))
    conn.commit()
    
    cursor.execute("SELECT id FROM customer WHERE name = ? and email = ? values(?,?)", (name_sql,email_sql,))
    alloted_id = cursor.fetchone()
    
    users_alloted_id = alloted_id[0] # for easy development
    '''
    
    
    # creating users personal table's name_variable where we can track him. 
    users_table_name = f"name:{name_sql} id:{users_alloted_id[0]}"
    '''
    conn.close()
    
    text = f'''
    ----------------------------------------------------------------------------------
    #   YOU NEED TO REMEMBER THIS DATA:
    #
    #   NAME     : {name}
    #   ID       : {users_alloted_id}
    #   PASSWORD : you know that.
    #   
    #   this data will halp you to interact with your account.
    ----------------------------------------------------------------------------------
    '''
    print(text)