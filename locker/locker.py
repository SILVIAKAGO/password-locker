import random
import string
users=[]
credentials=[]
class Credential:
    def __init__(self, acc_name, username, password):
        self.acc_name = acc_name
        self.username = username
        self.password = password
        
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Start:
    def main_page():
        print("\nSelect an option to proceed:")
        print("1.Add new\n2.Add existing\n3.View Account\n4.Delete Account")
        option = input()
        if option=="1":
            name=input("Enter site name: ")
            username=input("Enter username: ")
            print("Do you want a system generated password?\n1.Yes\n2.No")
            select = input()
            if select=="1":
                password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            elif select=="2":
                password=input("Enter password: ")
            else:
                print("Invalid option")
            cred = Credential(name,username,password)
            credentials.append(cred)
            print("Account added successfully")
            Start.main_page()
        elif option=="2":
            name=input("Enter site name: ")
            username=input("Enter username: ")
            password = input("Enter password: ")
            cred = Credential(name,username,password)
            credentials.append(cred)
            print("Account added successfully")
            Start.main_page()
        elif option=="3":
            for x in credentials:
                print("Site name: "+x.acc_name+" Username: "+x.username+" Password: "+x.password)
            Start.main_page()
        elif option=="4":
            print("Enter the name of the site you want to delete: ")
            accname=input()            
            for i, o in enumerate(credentials):
                if o.acc_name == accname:
                    del credentials[i]
                    break
            Start.main_page()
            
        else:
            print("Invalid option")
                    
    def login():
        print("\nLogin into your account:")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        for x in users:
            if x.username==username and x.password==password:
               Start.main_page()
            else:
                print("failed")
                
    def register():
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        user1 = User(username,password)
        users.append(user1)
        print("User Registered")
        Start.login()

print("Welcome!\nSelect an option to continue:")
print("1.Login\n2.Register\n3.Exit")
option = input()
if option=="1":
    print("Login Selected")
elif option=="2":
    Start.register()
elif option=="3":
    exit()
else:
    print("invalid option")