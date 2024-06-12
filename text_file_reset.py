def reset_text_files():
    
    name = open("name.txt", "w")
    name.write("")
    
    password = open("password.txt","w")
    password.write("")
    
    id = open("id.txt", "w")
    id.write("")
    
    table =  open("loged-in_users_table_name.txt","w")
    table.write("default")
    
    status = open("status.txt", "w")
    status.write("loged out")
    
    
