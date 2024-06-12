import sqlite3

def account_details():
    fileName = open("name.txt", 'r')
    name_sql = fileName.read()
    filePassword = open("password.txt",'r')
    password_sql = filePassword.read()
    fileId = open("id.txt", 'r')
    id_sql = fileId.read()
    
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM customer WHERE id =? AND name = ? AND password = ?", (id_sql, name_sql, password_sql,))
    values = cursor.fetchall()

    value = []
    
    for data in values:
        value = data
    
    print(f'''
       #  Name: {value[1]} 
       #  Id: {value[0]} 
       #  Amount: {value[4]} 
       #  Date of Birth: {value[3]} 
       #  Email: {value[5]} 
       #  Account Creating Date: {value[6]} 
       #  Account Creating Time: {value[7]}
           ''')
    
    conn.close()

