import sqlite3
from datetime import datetime

def command_str(command):
    
    file_name = open("name.txt",'r')
    read_name = file_name.read()
    
    file_id = open("id.txt", 'r')
    read_id = file_id.read()
    
    if read_name == '' and read_id == '':
        name_login = "default"
        id_login = 0
    elif read_name == '':
        name_login = "default"
    elif read_id == '':
        read_id = 0
    else:
        name_login = read_name
        id_login = read_id
        
    time = datetime.now()
    
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO history (name, command, execution_time, id) VALUES (?,?,?,?)", (name_login, command, formatted_time, id_login, ))
    conn.commit()
    conn.close()
    
