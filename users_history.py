import sqlite3
from datetime import datetime

time_ = datetime.now()

time = time_.strftime("%H:%M:%S")
date = time_.strftime("%Y-%m-%d")




def deposite_history(id , name , amount , deposite_amount , new_amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO deposite_history (date , time , id , name , amount , deposite_amount , new_amount) VALUES (?,?,?,?,?,?,?)",(date , time , id , name , amount , deposite_amount , new_amount ,))
    conn.commit()
    conn.close()



def withdrew_history(id , name , amount , withdrew_amount , new_amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO withdrew_history (date , time , id , name , amount , withdrew_amount , new_amount) VALUES (?,?,?,?,?,?,?)",(date , time , id , name , amount , withdrew_amount , new_amount ,))
    conn.commit()
    conn.close()



def send_money_history(id , name , amount , receiver_amount , receiver_id , receiver_name , new_amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO send_money_history (date , time , id , name , amount , receiver_amount , receiver_id , receiver_name , new_amount) VALUES (?,?,?,?,?,?,?,?,?)", (date , time , id , name , amount , receiver_amount , receiver_id , receiver_name , new_amount ,))
    conn.commit()
    conn.close()



def others_history():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    
    conn.commit()
    conn.close()