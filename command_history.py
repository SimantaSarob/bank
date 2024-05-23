import sqlite3
from datetime import datetime

def command_str(command):
    
    file = open("name.txt",'r')
    read = file.read()
    
    if read == '':
        name_login = "unresistered user"
    else:
        name_login = read
    time = datetime.now()
    #formatted_time = str(time)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO history (name, command, execution_time) VALUES (?,?,?)", (name_login, command, formatted_time, ))
    conn.commit()
    conn.close()
    
