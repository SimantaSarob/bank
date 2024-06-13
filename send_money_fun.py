import sqlite3
from users_history import send_money_history

def send_money(sender_id_txt, reciver_id_txt, amount_send_txt):

    sender_id = int(sender_id_txt)
    reciver_id = int(reciver_id_txt)
    amount_send = float(amount_send_txt)
    
    file_name = open("name.txt", 'r')
    name = file_name.read()
    file_password = open("password.txt", "r")
    password=file_password.read()
    
    
    # cheaking sender id is equal to login id.
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM customer WHERE name = ? and password = ?",(name, password,))
    login_id = cursor.fetchone()
    
    if sender_id == login_id[0] : #cheaking sender is the loginer or not.
        cursor.execute("select id from customer where id = ?",(reciver_id,)) 
        result_cheak = cursor.fetchone() # reciever id
        
        if result_cheak[0] == reciver_id:
            
            cursor.execute("select amount from customer where id = ?",(sender_id,))
            sender_old_amount = cursor.fetchone() # finding sender old amount to cheak if transition is possible or not.
            
            if sender_old_amount[0] >= amount_send:
                
                cursor.execute("select amount from customer where id = ?",(reciver_id,))
                old_amount = cursor.fetchone() # finding reciever old amount
                
                new_amount = old_amount[0] + amount_send
                cursor.execute("UPDATE customer SET amount= ? where id=?",(new_amount,reciver_id,))
                conn.commit() #updateing reciever amount   
                 
                sender_new_amount = sender_old_amount[0]- amount_send
                cursor.execute("UPDATE customer SET amount= ? where id=?",(sender_new_amount,sender_id,))
                conn.commit() # updating sender amount
                
                print("send done.")
                
                # start send money history keeping
                 
                file_name_ = open("name.txt", 'r')
                name_ = file_name_.read()
                
                cursor.execute("SELECT name FROM customer WHERE id = ?", (int(reciver_id),))
                receivers_name = cursor.fetchone()


                send_money_history(id = int(login_id[0]) , name = name_ , amount = int(sender_old_amount[0]) , receiver_amount = int(amount_send) , receiver_id = int(result_cheak[0]) , receiver_name = receivers_name[0]  , new_amount = int(sender_new_amount))
                # done send money history keeping
                
            else:
                print("not enougn money in your bank acount")
                conn.close()
                
        else:
            print("no reciver found.")
            conn.close()
        
    else:
        print("not your id.")
        conn.close()
