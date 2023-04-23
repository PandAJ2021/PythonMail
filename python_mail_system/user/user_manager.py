from user.user_model import User
from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
from exceptions import *


user_db_connector = PostgreSQLDatabase(
    dbname='postgres', user='postgres', password='1234')

users_db = DatabaseHandler('users', user_db_connector)

users_db.create_table({
    'id': 'bigserial primary key Not Null',
    'name': 'varchar(50)',
    'username':'varchar(50)',
    'salt': 'text Not Null',
    'password': 'text Not null'
})


class UserManager:

    @staticmethod
    def register_user(full_name: str, username: str, password: str):
        try:
            user = User(full_name, username, password)
            if not users_db.read(f"username = '{username}' and name = '{full_name.lower()}'"):
                users_db.insert(user.return_dict())
            else:
                raise UserAlreadyExist()
                
        except (InvalidNameFormat , InvalidPassword , InvalidUsername) as err:
            print(err)
            
        
