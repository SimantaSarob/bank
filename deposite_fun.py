import sqlite3
from users_history import deposite_history

def deposite(given_amount):
    file_name = open("name.txt", 'r') 
    name = file_name.read()
    file_password = open("password.txt", "r") 
    password = file_password.read()
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("SELECT amount FROM customer WHERE name = ? AND password = ?",(name,password,))
    value = cursor.fetchone()
    deposite_total = value[0] + float(given_amount)
    
    cursor.execute("UPDATE customer SET amount= ? where name= ? AND password = ?",(deposite_total, name, password,))
    conn.commit()
    conn.close()
    print("deposite done.")
    
    
    # starting deposite history keeping
    
    file_id = open("id.txt", "r")
    id = file_id.read() # id number
    amount = float(value[0])
    deposite_amount = given_amount
    new_amount = deposite_total
    
    deposite_history(id , name, amount , deposite_amount , new_amount)
    
    # done deposite history keeping
    
    
    

