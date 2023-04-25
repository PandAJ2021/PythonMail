from user.user_model import User
from datastore.tables  import get_users_db
from exceptions import *
import hashlib


class UserManager:

    users_db = get_users_db()
    user = User

    @classmethod
    def auth_username(cls, username):
        # stored users is a list of one member tuples.
        stored_users = cls.users_db.read(
            'username', f"username = '{username}'")
        return username in [t[0] for t in stored_users]

    @classmethod
    def auth_pass(cls, username, password):
        salt, stored_pass = cls.users_db.read(
            columns='salt, password', condition=f"username = '{username}'")[0]
        entered_pass = password + salt
        hashed_entered = hashlib.md5(entered_pass.encode()).hexdigest()
        return hashed_entered == stored_pass
    
    @classmethod
    def get_id(cls, username):
        if not UserManager.auth_username(username):
            raise UserNotFound
        user_id = cls.users_db.read('user_id', f"username = '{username}'")[0][0]
        return user_id

    @classmethod
    def get_username_from_id(cls , id):
            username = cls.users_db.read('username', f"user_id = '{id}'")[0][0]
            if not username:
                raise UserNotFound
        

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
            return cls.get_id(username)
        except AuthenticationError as err:
            print(err)
            
    @classmethod
    def logout(cls, username):
        cls.users_db.update({'logging': False}, f"username = '{username}'")


