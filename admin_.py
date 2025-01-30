import time
from doc_fun import admin_doc
import sqlite3
from clear_fun import clear
import os

conn = sqlite3.connect("bank.db")
cur = conn.cursor()

def admin():
    while True:
        command = input("Bank : Admin > ")
        time.sleep(0.01)
        if command == "doc" or "help":
            admin_doc()
            
        elif command == "customer":
            conn = sqlite3.connect("bank.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM customer")
            customer_data = cur.fetchall()
            conn.close()
            
            for data in customer_data:
                print(data)
        
        elif command == "exit":
            break
            
        elif command == "clear":
            clear()
        
        elif command == "history":
            conn = sqlite3.connect("bank.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM history")
            history_data = cur.fetchall()
            conn.close()
            for data in history_data:
                print(data)
        
        elif command == "system":
            print("\nSystem Level Access Grunted.\nCarefull what you do.\nUse 'exit' to go back to Admin access.\n")
            while True:
                cmd = input("Bank : Admin : System > ")
                os.system(cmd)
                if cmd == "exit":
                    break
                
        elif command == "db":
            print("\nBank Database Access Grunted.\nCarefull what you do.\nUse 'exit' to go back to Admin access.\n")
            conn = sqlite3.connect("bank.db")
            cur = conn.cursor()
            while True: 
                sql = input("Bank : Admin : bank.db (sql) > ")
                if sql == "exit":
                    break
                cur.execute(sql)
                all_data = cur.fetchall()
                for data in all_data:
                    print(data)
        
        else:
            print("Not A valid Admin Command.")
