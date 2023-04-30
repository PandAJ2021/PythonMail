from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
from user.user_manager import UserManager
from massage.email_manager import EmailManager
from utils.user_interface import Menu , Menu_item
from datetime import datetime

class ManageProgram:

    user = UserManager
    email = EmailManager
    user_id = None

    @classmethod
    def register(cls):
        name = input('Enter your full name : ')
        username = input('Enter your username: ')
        passwd = input('Enter your password: ')
        cls.user.register_user(name , username , passwd)

    @classmethod
    def log_in(cls):
        username = input('Enter your username: ')
        passwd = input('Enter your password: ')   
        cls.user_id = cls.user.logging_user(username, passwd)

    @classmethod
    def log_out(cls):
        if cls.user_id :
            user_id = cls.user.logout(cls.user_id)
        user_id = None
    
    #Mj12345678
    @classmethod
    def send_msg(cls):
        print('\n===== Sending massage =====\n')
        subject = input("Enter the subject: ")
        body = input("Enter your massage: ")
        receiver_usrname = input("Enter receiver username: ")
        recip_id = cls.user.get_id(receiver_usrname)
        if recip_id:
            massage_id = cls.email.make_massage(subject, body, cls.user_id, recip_id)
            ask = input('Do you want to send massage? (Y/n)')
            if ask[0] in 'Nn':
                print('massage saved in draft.')
            else :
                cls.email.send_massage(massage_id)
                print('massage sent successfully.')
        
    @classmethod
    def inbox(cls):
        if cls.user_id :
            a= cls.email.show_inbox(cls.user_id) 
            for tup in a :
                print(f"\nfrom {cls.user.get_username_from_id(tup[0])}",
                f", 'subject': {tup[1]}, 'received in': {tup[3].ctime()}, 'read_state': {tup[4]}" ,
                f", 'massage': (({tup[2]}))")
            
    @classmethod
    def sentbox(cls):
        if cls.user_id :
            a= cls.email.show_sentbox(cls.user_id)
            for tup in a :
                print(f"\nto {cls.user.get_username_from_id(tup[0])}",
                f", 'subject': {tup[1]}, 'send in': {tup[3].ctime()}" ,
                f", 'massage': (({tup[2]}))")

    @classmethod 
    def draft(cls):
        if cls.user_id :
            a= cls.email.show_draft(cls.user_id)
            for tup in a :
                print(f"\nto {cls.user.get_username_from_id(tup[0])}",
                f", 'subject': {tup[1]}, 'send in': {tup[3].ctime()}" ,
                f", 'massage': (({tup[2]}))")
        


routers = Menu_item('Login or Register', children = [
    Menu_item('Sign up' ,function= ManageProgram.register),
    Menu_item('Sign in' ,function= ManageProgram.log_in) ,
    Menu_item('User Panel' , condition= UserManager.get_user_status, children=[
        Menu_item('Send massage', function= ManageProgram.send_msg),
        Menu_item('Sent box', function= ManageProgram.sentbox),
        Menu_item('inbox' , function= ManageProgram.inbox ),
        Menu_item('Draft', function= ManageProgram.draft),
        ]) , 
    Menu_item('Logout',condition= UserManager.get_user_status , function= ManageProgram.log_out)])


Menu.run_menu(routers)
