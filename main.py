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
        #print("\n")
        command_str(command)
        sleep(0.1)
        
        if command == "exit" : # exit
            name = ''
            password = ''
            id = ''
            logout(name, password, id)
            break
        
        elif command == "total": # total money
            total()
        
        elif command == "login": # login and pass encrypt
            
            logout(name='',password='', id='') #added this line because of, if someone do login and use login command again, his/her previous login details will be eraised.
            
            name = input("name: ")
            id = input("user id: ")
            plain_password  = input("password: ")
            password = hashlib.sha256(plain_password.encode()).hexdigest()
            
            conn = sqlite3.connect('bank.db')
            cursor = conn.cursor()  
            cursor.execute("SELECT id FROM customer WHERE name = ? AND password = ? ",(name,password,))
            value = cursor.fetchone()
            
            if value is not None and int(value[0])==int(id):
                print("Loged in successful.")
                login(name,password,id)
            else:
                print("Name or password is not correct.")
                
            conn.close()
            
                
        elif command == "logout": #log out 
            name = ''
            password = ''
            id = ''
            logout(name,password,id)
            print("Logout done.")
        
        elif command == "signup": #sign up
            name = input("your name: ")
            dob = input("Your date of birth (YYYY-MM-DD): ")
            amount = input("The amount of money you want to keep in the bank: ")
            plain_password  = input("Type your password: ")
            plain_password_again  = input("Type your password again: ")
            
            if plain_password == plain_password_again:
                password = hashlib.sha256(plain_password.encode()).hexdigest() 
                
            else:
                print("Try again later with 'signup' command.")
                
            signup(name, password, dob, amount)
            
        elif command == "doc": #documentation
            doc()
        
        elif command =="deposite": #deposite
            given_amount = input("Amount: ")
            deposite(given_amount)

        elif command =="withdrew": #withdrew
            given_amount = input("Amount: ")
            withdrew(given_amount)
        
        elif command == "id":
            name = input("Name: ")
            id_num(name) 
        
        elif command == "login details":
            
            file = open("name.txt",'r')
            name = file.read()
            
            if name =="":
                print("Name: Null")    
            else:
                print(F"Name: {name}")
                
            id_num(name)
        
        elif command == "send money":
            sender_id_txt = input("YOUR ID: ")
            reciver_id_txt = input("RECIVER ID: ")
            amount_send_txt = input("The amount you want to sent: ")
            
            send_money(sender_id_txt, reciver_id_txt, amount_send_txt)
            
        else:
            print("not valid command. use 'doc' command to see all the valid command/s.")
            
        #print("\n")
        
main()