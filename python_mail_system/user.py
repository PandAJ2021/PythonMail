import re
from exceptions import *

class User:
    users = []
    def __init__(self , full_name , username , password):
        self.full_name = full_name
        self.username = username
        self.password = password

    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self , name):
        #pattern: start by bounch of letters and pass with 1-3 group of space+letters
        if not re.match(r'^[a-zA-Z]+( [a-zA-Z]+){1,5}$', name):
            raise InvalidNameFormat()
        self._full_name = name 

    @property
    def username(self):
        return self._username 
    
    @username.setter
    def username(self , value):
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[_\-.])[a-zA-Z0-9_\-.]+$', value):
            raise InvalidUsername()
        self._username = value

# test = User('ali jalili', 'Ali-jalili', 'password')