class AuthException(Exception):
    pass


class InvalidNameFormat(AuthException):
    def __init__(self):
        super().__init__('Invalid name format: your name does not match the required format. ' +
                         'Please enter a valid \nname with two or more sections,' +
                         'each separated by a single space and containing only letters!')


class InvalidUsername(AuthException):
    def __init__(self):
        super().__init__("Invalid username format: usernames must contain at least one" +
                         " uppercase letter, one\n digit, and one of the characters '_', '-', or '.' ")


class InvalidPassword(AuthException):
    def __init__(self):
        super().__init__('Password must be at least 8 characters long and contain at least one' +
                         ' uppercase letter and one digit!')


class UserNameAlreadyExist(AuthException):
    def __init__(self):
        super().__init__('Sorry, that username is already taken. Please choose a different username.!')


class AuthenticationError(AuthException):
    def __init__(self):
        super().__init__('The username or password you entered is incorrect. Please try again!')


class UserNotFound(AuthException):
    def __init__(self):
        super().__init__('Sorry, we could not find a user with that username!')

class EmptyFieldError(AuthException):
    def __init__(self):
        super().__init__('This field cannot be empty!')
