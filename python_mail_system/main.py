from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
from user.user_manager import UserManager
from massage.email_manager import EmailManager
from utils.user_interface import Menu , Menu_item

    
def register():
    name = input('Enter your full name : ')
    username = input('Enter your username: ')
    passwd = input('Enter your password: ')
    UserManager.register_user(name , username , passwd)
    # print("You sign up successfully")

def log_in():
    username = input('Enter your username: ')
    passwd = input('Enter your password: ')   
    global user_id
    user_id = UserManager.logging_user(username, passwd)

def inbox():
    a= EmailManager.show_inbox(user_id)   
    print(a)

user_id = 1

routers = Menu_item('Login or Register',condition =True ,  children = [
    Menu_item('Sign up' ,condition= True , function=register),
    Menu_item('Sign in' , condition= True,function=log_in) ,
    Menu_item('User Panel' , condition= UserManager.user_status, children=[
        Menu_item('Send massage'),
        Menu_item('Sent box'),
        Menu_item('inbox' , function= inbox ),
        Menu_item('Draft'),
        ]) , 
    Menu_item('Logout')])


Menu.run_menu(routers)
# print(user_id)

# log_in()