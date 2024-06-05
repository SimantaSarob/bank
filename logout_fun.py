from login_fun import login

def logout(name, password, id):
    name = ''
    password = ''
    id = ''
    login(name, password, id)
    
    file_status = open("status.txt", 'w')
    file_status.write("loged out")
    
    