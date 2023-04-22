import re
import secrets
import hashlib
from exceptions import *


class User:
    users = []

    def __init__(self, full_name: str, username: str, password: str):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.salt = secrets.token_hex(15)
        __class__.users.append(self)

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, name):
        # pattern: start by bounch of letters and pass with 1-3 group of space+letters
        if not re.match(r'^[a-zA-Z]+( [a-zA-Z]+){1,5}$', name):
            raise InvalidNameFormat()
        self._full_name = name

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
        hashed = hashlib.md5(passwd.encode())
        self._password = hashed

