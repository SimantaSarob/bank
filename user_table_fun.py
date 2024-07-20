import sqlite3


def make_users_table_name(name, id):
    
    name_mod = name.replace(" ","_")
    
    users_table_name = f"{name_mod}_id_{id}"
    file = open("loged-in_users_table_name.txt","w")
    file.write(users_table_name)
    
    create_users_table(str(users_table_name))

def create_users_table(users_table_name):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {users_table_name} (event_no INTEGER, date DATETIME, time	DATETIME, amount	INTEGER,  command	TEXT, t_amount	INTEGER , sent_amount	INTEGER ,sent_id integer, name	TEXT , deposit_amount	INTEGER , withdrew_amount	INTEGER , new_amount integer, PRIMARY KEY(event_no AUTOINCREMENT))")
    conn.commit()
    conn.close()
