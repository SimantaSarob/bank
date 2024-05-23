import sqlite3

def total():
    fileName = open("name.txt", 'r')
    name_sql = fileName.read()
    filePassword = open("password.txt",'r')
    password_sql = filePassword.read()
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("SELECT amount FROM customer WHERE name = ? AND password = ?",(name_sql,password_sql,))
    value = cursor.fetchone()
    print(value[0])
    conn.close()
    