
def login(name, password, id):
    
    file_name = open("name.txt", 'w') # save name
    file_name.write(name)
    
    file_password = open("password.txt", "w") # save pass hash
    file_password.write(password)
    
    file_id = open("id.txt", "w") # save idd number
    file_id.write(id)
    
    file_status = open("status.txt", 'w') # loged in or loged out status keeper file
    file_status.write("loged in")
