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
            values = cursor.fetchall()
            
            ids = []    # collectinh multiple values in tauple
            for value in values:
                ids.append(value[0])
                
            size = len(ids)     # finding the size of the tauple for while loop's break condition.
            start = 0
            
            while True:
                print(f"id: {ids[start]}")  # printing the data.
                start = start + 1
                if start == size:
                    break
                
            conn.close()
        
        else:
            print(f"no one found with provided name:'{name}'")
            conn.close()
