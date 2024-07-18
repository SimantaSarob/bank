import sqlite3

def id_num(name):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()  
    
    cursor.execute("SELECT COUNT(*) FROM customer WHERE name = ?",(name,))
    result = cursor.fetchone()
    if name == "":
        print("id: Null \nNo Name Entered.")
        
    else:
        if result[0]>0:
            cursor.execute("SELECT id FROM customer WHERE name = ? ",(name,))
            values = cursor.fetchall()
            
            ids = []    # collecting multiple values in tauple
            for value in values:
                ids.append(value[0])
                
            size = len(ids)     # finding the size of the tauple for while loop's break condition.
            start = 0
            
            while True:
                print(f"id: {ids[start]}")  # printing the data.
                start = start + 1
                if start == size:
                    break
                
            if size > 1:    #if theres more then 1 id, we need more data from users.
                print("we need more information to find one specific name's id. \nSo, if you want to find the ID you need to give us more info about him.")
                DateOfBirth = input(f"{name}'s Death Of Birth (YYYY-MM-DD): ")
                
                if DateOfBirth == "":
                    print("You didn't entry the DOB. sorry, we can't help you without this info.")
                
                elif DateOfBirth:
                    #  fetching dob of given name
                    cursor.execute("select id from customer where name=? and dob = ?",(name,DateOfBirth,))
                    result_cheak_dob=cursor.fetchall()
                    
                    result_cheak_dob_list = []  # creating list of our result.
                    
                    for result in result_cheak_dob:
                        result_cheak_dob_list.append(result[0])   # puting results into this list
                    
                    for list_item in result_cheak_dob_list:
                        print(list_item)    # printing list items.
                
                else:
                    print("Not a vaild birthdate. Or your client didn't opened any account in this bank.")
                
            conn.close()
        
        else:
            print(f"no one found with provided name:'{name}'")
            conn.close()
