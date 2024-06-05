import sqlite3

def login_details():
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
    
    print(f"\nName: {value[1]} \nId: {value[0]} \nAmount: {value[4]} \nDate of Birth: {value[3]} \nEmail: {value[5]} \nAccount Creating Date: {value[6]} \nAccount Creating Time: {value[7]}\n")
    
    conn.close()
