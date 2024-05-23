import sqlite3

def id_num(name):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    
    cursor.execute("SELECT COUNT(*) FROM customer WHERE name = ?",(name,))
    result = cursor.fetchone()
    if name == "":
        print("id: Null")
        
    else:
        if result[0]>0:
            cursor.execute("SELECT id FROM customer WHERE name = ? ",(name,))
            value = cursor.fetchone()
            print(f"id: {value[0]}")
            conn.close()
        
        else:
            print(f"no one found with provided name:{name}")
            conn.close()
