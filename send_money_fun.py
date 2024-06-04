import sqlite3

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
    
    if sender_id == login_id[0] :
        cursor.execute("select id from customer where id = ?",(reciver_id,))
        result_cheak = cursor.fetchone() #cheaking sender is the loginer or not.
        
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
                conn.close()
                
            else:
                print("not enougn money in your bank acount")
                conn.close()
                
        else:
            print("no reciver found.")
            conn.close()
        
    else:
        print("not your id.")
        conn.close()
