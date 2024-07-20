import user_table_fun
####################################
#                                  #
#   full logic in main.py file.    #
#                                  #
####################################

def login(name, password, id):
    
    file_name = open("name.txt", 'w') # save name
    file_name.write(name)
    
    file_password = open("password.txt", "w") # save pass hash
    file_password.write(password)
    
    file_id = open("id.txt", "w") # save id number
    file_id.write(id)
    
    file_status = open("status.txt", 'w') # loged in or loged out status keeper file
    file_status.write("loged in")
    
    
    # creating users personal table's name_variable where we can track him. 
    user_table_fun.make_users_table_name(name,id)