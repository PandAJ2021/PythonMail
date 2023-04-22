class AuthException(Exception):
    pass


class InvalidNameFormat(AuthException):
    def __init__(self):
        super().__init__('Invalid format: your name does not match the required format.' +
                         'Please enter a valid \nname with two or more sections,' +
                         'each separated by a single space and containing only letters.')


class InvalidUsername(AuthException):
    def __init__(self):
        super().__init__("Invalid username format: usernames must contain at least one" +
                         " uppercase letter, one\n digit, and one of the characters '_', '-', or '.' ")


class InvalidPassword(AuthException):
    def __init__(self):
        super().__init__('Password must be at least 8 characters long and contain at least one'+ 
                    ' uppercase letter and one\n digit.')
