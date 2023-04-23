from user.user_model import User
from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
from exceptions import *
import hashlib


user_db_connector = PostgreSQLDatabase(
    dbname='postgres', user='postgres', password='1234')

users_db = DatabaseHandler('users', user_db_connector)

users_db.create_table({
    'id': 'bigserial primary key Not Null',
    'name': 'varchar(50)',
    'username': 'varchar(50)',
    'salt': 'text Not Null',
    'password': 'text Not null',
    'logging' : 'boolean default false'
})



class UserManager:


    @staticmethod
    def auth_username(username):
        # stored users is a list of one member tuples.
        stored_users = users_db.read('username', f"username = '{username}'")
        return username in [t[0] for t in stored_users]
        

    @staticmethod
    def auth_pass(username, password):
        salt, stored_pass = users_db.read(
            columns='salt, password', condition=f"username = '{username}'")[0]
        entered_pass = password + salt
        hashed_entered = hashlib.md5(entered_pass.encode()).hexdigest()
        return hashed_entered == stored_pass


    @staticmethod
    def register_user(full_name: str, username: str, password: str):
        try:
            user = User(full_name, username, password)
            if UserManager.auth_username(username):
                raise UserNameAlreadyExist
            users_db.insert(user.dict_attribute())
        except (InvalidNameFormat, InvalidPassword, InvalidUsername, UserNameAlreadyExist) as err:
            print(err)

    @staticmethod
    def logging_user(username:str, password:str):
        try:
            if not UserManager.auth_username(username) and UserManager.auth_pass(username, password):
                raise AuthenticationError
            users_db.update({'logging':True}, f"username = '{username}'")
        except (InvalidPassword, InvalidUsername , AuthenticationError) as err:
            print(err)
        

    