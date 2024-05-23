import sqlite3

def withdrew(given_amount):
    file_name = open("name.txt", 'r') 
    name = file_name.read()
    file_password = open("password.txt", "r") 
    password = file_password.read()
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("SELECT amount FROM customer WHERE name = ? AND password = ?",(name,password,))
    value = cursor.fetchone()
    
    if int(given_amount) <= value[0]: 
        withdrew_total = value[0] - int(given_amount)
        cursor.execute("UPDATE customer SET amount= ? where name= ? AND password = ?",(withdrew_total, name, password,))
        conn.commit()
        conn.close()
        print("withdrew done.")
    else:
        print(f"you don't have that much money in your account to withdrew {given_amount}. you have only {value[0]} money left. ")
        conn.close()
    
    
    

