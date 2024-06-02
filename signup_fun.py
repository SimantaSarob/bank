import sqlite3

def signup(name, password, dob, amount):
    name_sql = name
    password_sql = password
    dob_sql = dob
    amount_sql = int(amount)
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO customer (name,password,dob,amount) VALUES(?,?,?,?)",(name_sql,password_sql, dob_sql, amount_sql,))
    conn.commit()
    conn.close()
    
    print("ok. done.")