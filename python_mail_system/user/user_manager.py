from user.user_model import User
from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
import hashlib
from utils.tables import get_users_db
from exceptions import *



class UserManager:

    users_db = get_users_db()
    user = User

    @classmethod
    def auth_username(cls, username):
        # stored users is a list of one member tuples.
        stored_users = cls.users_db.read('username', f"username = '{username}'")
        return username in [t[0] for t in stored_users]

    @classmethod
    def auth_pass(cls, username, password):
        salt, stored_pass = cls.users_db.read(
            columns='salt, password', condition=f"username = '{username}'")[0]
        entered_pass = password + salt
        hashed_entered = hashlib.md5(entered_pass.encode()).hexdigest()
        return hashed_entered == stored_pass

    @classmethod
    def register_user(cls, full_name: str, username: str, password: str):
        try:
            my_user = cls.user(full_name, username, password)
            if cls.auth_username(username):
                raise UserNameAlreadyExist
            cls.users_db.insert(my_user.dict_attribute())
        except (InvalidNameFormat, InvalidPassword, InvalidUsername, UserNameAlreadyExist) as err:
            print(err)

    @classmethod
    def logging_user(cls, username: str, password: str):
        try:
            if not cls.auth_username(username) and cls.auth_pass(username, password):
                raise AuthenticationError
            cls.users_db.update({'logging': True}, f"username = '{username}'")
            user_row = cls.users_db.read(
                'id, name , username', f"username = '{username}'")[0]
            my_user = cls.user(user_row[1],user_row[2],"FakePass1",user_row[0] )
            #becuse I dont need passwd and can't use hash pass here
            return my_user
        except AuthenticationError as err:
            print(err)

    @classmethod
    def get_id(username):
        if not UserManager.auth_username(username):
            raise UserNotFound
        user_id = cls.users_db.read('id', f"username = '{username}'")[0][0]
        return user_id
