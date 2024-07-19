import time
from doc_fun import admin_doc
import sqlite3
from clear_fun import clear

def admin():
    while True:
        command = input("Admin : ")
        time.sleep(0.01)
        if command == "doc":
            admin_doc()
            
        elif command == "customer":
            conn = sqlite3.connect("bank.db")
            cur = conn.cursor()
            
            cur.execute("SELECT * FROM customer")
            customer_data = cur.fetchall()
            
            for data in customer_data:
                print(data)
        
        elif command == "exit":
            break
            
        elif command == "clear":
            clear()
        
        else:
            print("Not A valid Admin command.")
