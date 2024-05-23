import hashlib
import sqlite3
from time import sleep
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


print("for documentation type doc and enter.")

def main():
    while True:
        command = input("Bank > ")
        command_str(command)
        sleep(0.1)
        
        if command == "exit" : # exit
            name = ''
            password = ''
            logout(name , password)
            break
        
        elif command == "total": # total money
            total()
        
        elif command == "login": # login and pass encrypt
            
            logout(name='',password='') #added this line because of, if someone do login and use login command again, his/her previous login details willbe eraised.
            
            name = input("name: ")
            plain_password  = input("password: ")
            password = hashlib.sha256(plain_password.encode()).hexdigest()
            conn = sqlite3.connect('bank.db')
            cursor = conn.cursor()  
            cursor.execute("SELECT id FROM customer WHERE name = ? AND password = ?",(name,password,))
            value = cursor.fetchone()
            
            if value is not None:
                print("loged in successful.")
                login(name,password)
            else:
                print("name or password is not correct.")
                
            conn.close()
            
                
        elif command == "logout": #log out 
            name = ''
            password = ''
            logout(name,password)
            print("logout done.")
        
        elif command == "signup": #sign up
            name = input("your name: ")
            dob = input("your date of birth: ")
            amount = input("the amount of money you want to keep in the bank: ")
            plain_password  = input("type your password: ")
            plain_password_again  = input("type your password again: ")
            if plain_password == plain_password_again:
                password = hashlib.sha256(plain_password.encode()).hexdigest()
            else:
                print("try again with signup command.")
            signup(name, password, dob, amount)
            
        elif command == "doc": #documentation
            doc()
        
        elif command =="deposite": #deposite
            given_amount = input("amount: ")
            deposite(given_amount)

        elif command =="withdrew": #withdrew
            given_amount = input("amount: ")
            withdrew(given_amount)
        
        elif command == "id":
            name = input("name: ")
            id_num(name) 
        
        elif command == "login details":
            file = open("name.txt",'r')
            name = file.read()
            if name =="":
                print("name: Null")
            else:
                print(F"name: {name}")
            id_num(name)
        
        elif command == "send money":
            sender_id_txt = input("YOUR ID: ")
            reciver_id_txt = input("RECIVER ID: ")
            amount_send_txt = input("amount: ")
            send_money(sender_id_txt, reciver_id_txt, amount_send_txt)
            
        else:
            print("not valid command. use 'doc' command to see all the valid command/s.")
        
main()