
def login(name, password, id):
    file_name = open("name.txt", 'w') # save name
    file_name.write(name)
    file_password = open("password.txt", "w") # save pass hash
    file_password.write(password)
    file_id = open("id.txt", "w")
    file_id.write(id)
