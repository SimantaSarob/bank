def doc():
    print(f'''
+------------------------------------------------------------------------------------+
| Hello! It's a demo banking system which is made and maintain by Simanta Saha Sarob.|
+---------------+--------------------------------------------------------------------+
| Command       | Discripytion                                                       |
+---------------+--------------------------------------------------------------------+
| login         | Log in your account. Give your account name, ID and password.      |
| admin         | Total access of Bank. (Under DEvelopment.)                         |
| logout        | Log out from your profile.                                         |
| exit          | Will exit the code.                                                |
| doc           | For documentation.                                                 |
| total         | Will give you the amount of money you stored in your bank account. |
| deposite      | To deposite your money.                                            |
| withdrew      | Withdrew your money.                                               |
| id            | Find someones name through different informations.                 |
| login details | Show everything about account.                                     |
| send money    | Send money to Different users. (Need to know recievers ID number.) |
| signup        | Create an account. (Need to fill some personal data)               |
| clear         | Clear the interface.                                               |
+---------------+--------------------------------------------------------------------+
''')


def admin_doc():
    print('''
+----------+--------------------------------------------------------------+
|  Command |                         Discription                          |
|----------|--------------------------------------------------------------+
| system   | Will give you system access. (NOT RECOMENDED) (Only in linux)|
| db       | Direct access to the Main Database (bank.db). (WARNING: Do   |
|          | not use this command untill you know what you are doing.)    |
| help     | Will show you this message.                                  |
| doc      | Will show you this message.                                  |
| history  | Will Show You All Data From History Table.                   |
| clear    | Will clear the screen.                                       |
| exit     | Will exit from `Admin` access  and return Back to normal     |
|          | user access.                                                 |
| customer | Will show you all the data of Customers aka users.           |
+----------+--------------------------------------------------------------+
          ''')