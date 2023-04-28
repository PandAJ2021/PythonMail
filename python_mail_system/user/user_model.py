import re
import secrets
import hashlib
from exceptions import *


class User:

    def __init__(self, full_name: str, username: str, password: str , user_id=None):
        self.id = user_id
        self.full_name = full_name
        self.username = username
        self.salt = secrets.token_hex(15)
        self.password = password
    
    def dict_attribute(self):

        return { 
            "name": f"'{self.full_name}'",
            "username": f"'{self.username}'",
            "salt": f"'{self.salt}'",
            "password": f"'{self.password}'"
            }
    # def logging_status(self):
    #     return self.login
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, name):
        # pattern: start by bounch of letters and pass with 1-3 group of space+letters
        if not re.match(r'^[a-zA-Z]+( [a-zA-Z]+){1,5}$', name):
            raise InvalidNameFormat()
        self._full_name = name.upper()

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[_\-.])[a-zA-Z0-9_\-.]+$', value):
            raise InvalidUsername()
        self._username = value


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', value):
            raise InvalidPassword()
        passwd = value + self.salt
        hashed = hashlib.md5(passwd.encode()).hexdigest()
        self._password = hashed

