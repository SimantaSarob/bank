#!/usr/bin/python
import hashlib
import sqlite3
from time import sleep
from text_file_reset import reset_text_files
from login_fun import login
from logout_fun import logout
from signup_fun import signup
from total_fun import total
from doc_fun import doc
from deposite_fun import deposite
from withdrew_fun import withdrew
from id_num_fun import id_num
from send_money_fun import send_money
from command_history import command_str
from account_details_fun import account_details
import admin_
from clear_fun import clear

reset_text_files()
doc()
def main():
    while True:
        cmd = input("Bank > ")
        command = cmd.lower()

        command_str(command)
        sleep(0.1)
        
        if command == "exit" : # exit
            reset_text_files()
            break
        
        elif command == "total": # total money
            file_status = open("status.txt", 'r')
            active_status = file_status.read()
            
            if active_status == "loged in":
                total()
                
            else:
                  print("Please Login first. If you don't have an account,please signup to creat one.")


        elif command == "login": # login and pass encrypt
            file_ = open("status.txt","r")
            status = file_.read()

            if status == "loged in": # cheaking if someone is loged in or not.
                name_ = open("name.txt","r")
                name = name_.read()
                id_ = open("id.txt","r")
                id = id_.read()
                
                print(f"You are curently loged in as {name} and ID:{id}. Please do logout first.") # giving the current loged in account details
                
            else: # if no one in loged in
                name = input("Name: ")
                id = input("User id: ")
                plain_password  = input("Password: ")
                
                empty = [" ",""]
                
                if name in empty or id in empty or plain_password in empty: # this will cheak if user's input is valid or not.
                    print("You didn't filled one or more inforamtion field. Please Try Again Later.")
                    
                else: # if every inputed data is acceptable data
                    password = hashlib.sha256(plain_password.encode()).hexdigest()
                    
                    conn = sqlite3.connect('bank.db')
                    cursor = conn.cursor()  
                    cursor.execute("SELECT password FROM customer WHERE name = ? AND id = ? ",(name,id,))
                    value = cursor.fetchone()
                    
                    if value is not None and str(value[0])==str(password): # login confermation.
                        clear() # clearing the shell to ensure no one sees the plain password which is entered.
                        print(f"Loged in as {name} successful.")
                        login(name,password,id)
                        
                        conn.close()
                    else: # given data in not in db.
                        print("Name, password or id is not valid. Please try again later.")
            
                
        elif command == "logout": #log out 
            file_ = open("status.txt","r")
            status = file_.read()
            
            if status == "loged out":
                print("You didn't loged in yet.")

            else:
                reset_text_files()
                print("Logout done.")
        
        
        elif command == "signup": #sign up
            file_ = open("status.txt","r")
            status = file_.read()
            
            if status == "loged in":
                print("Please log out first to creat New Account.")
            else:
                name = input("Your name: ")
                dob = input("Your date of birth (YYYY-MM-DD): ")
                amount = input("The amount of money you want to keep in the bank: ")
                email = input("Email: ")
                plain_password  = input("Type your password: ")
                plain_password_again  = input("Type your password again: ")
                
                if plain_password == plain_password_again:
                    password = hashlib.sha256(plain_password.encode()).hexdigest()
                    
                    signup(name, password, dob, amount, email)

                    
                else:
                    print("Password didnt matched. \nTry again with 'signup' command.")
                    
        
        
        elif command == "doc": #documentation
            doc()
      
        
        elif command =="deposite": #deposite
            
            file_status = open("status.txt", 'r')
            active_status = file_status.read()
            
            if active_status == "loged in":
                given_amount = input("Amount: ")
                deposite(given_amount)
                
            else:
                print("Please Login first. If you don't have an account, please do signup to create one.")


        elif command =="withdrew": #withdrew
            file_status = open("status.txt", 'r')
            active_status = file_status.read()
            
            if active_status == "loged in":
                given_amount = input("Amount: ")
                withdrew(given_amount)
                
            else:
                print("Please Login first. If you don't have an account,please signup to create one.")
 
        
        elif command == "id":
            file_status = open("status.txt", 'r')
            active_status = file_status.read()
            
            if active_status == "loged in":
                name = input("Name: ")
                id_num(name)
                
            else:
                print("Please Login first. If you don't have an account,please signup to create one.")
    
        
        elif command == "account details":
            file_status = open("status.txt", 'r')
            active_status = file_status.read()
            
            if active_status == "loged in":
                account_details()
            
            else:
                print("Please Login first. If you don't have an account, please signup to create one.")
            
                
        elif command == "send money":
            file_status = open("status.txt", 'r')
            active_status = file_status.read()
            
            if active_status == "loged in":
                
                sender_id_txt = input("YOUR ID: ")
                reciver_id_txt = input("RECIVER ID: ")
                amount_send_txt = input("The amount you want to sent: ")
            
                send_money(sender_id_txt, reciver_id_txt, amount_send_txt)
                
            else:
                print("Please Login first. If you don't have an account, please signup to create one.")

        
        elif command == "clear": # clear the shell.
            clear()

        elif command == "admin":
            file_ = open("name.txt","r")
            name = file_.read()
            file__ = open("id.txt")
            id = file__.read()
            file_status = open("status.txt")
            status = file_status.read()
            
            if status == "loged out":
                print("Please login first")
            else:
                if name == "Admin" and id == "1":
                    passwd_input = input("Admin Password:")
                    password_hash = hashlib.sha256(passwd_input.encode()).hexdigest()
                    
                    conn = sqlite3.connect("bank.db")
                    cursor = conn.cursor()
                    
                    cursor.execute("SELECT password FROM customer WHERE name = 'Admin' and id = 1")
                    password_from_db = cursor.fetchone()
                    
                    if password_from_db[0] == password_hash:
                        admin_.admin()
                        
                    else:
                        print("Admin Password Didn't Matched.")
                    
                else:
                    print("Login as Admin.")
                
        
        else:
            print("Not valid command. Use 'doc' command to see all the valid command(s).")
            

main()
