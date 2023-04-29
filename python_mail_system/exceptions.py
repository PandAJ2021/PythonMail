class AuthException(Exception):
    pass


class InvalidNameFormat(AuthException):
    def __init__(self):
        super().__init__('\nInvalid name format: your name does not match the required format. ' +
                         'Please enter a valid \nname with two or more sections,' +
                         'each separated by a single space and containing only letters!')


class InvalidUsername(AuthException):
    def __init__(self):
        super().__init__("\nInvalid username format: usernames must contain at least one" +
                         " uppercase letter, one\n digit, and one of the characters '_', '-', or '.' ")


class InvalidPassword(AuthException):
    def __init__(self):
        super().__init__('\nPassword must be at least 8 characters long and contain at least one' +
                         ' uppercase letter and one digit!')


class UserNameAlreadyExist(AuthException):
    def __init__(self):
        super().__init__('\nSorry, that username is already taken. Please choose a different username.!')


class AuthenticationError(AuthException):
    def __init__(self):
        super().__init__('\nThe username or password you entered is incorrect. Please try again!')


class UserNotFound(AuthException):
    def __init__(self):
        super().__init__('\nSorry, we could not find a user with that username!')


class EmptyFieldError(AuthException):
    def __init__(self):
        super().__init__('\nThis field cannot be empty!')

class InvalidIndexError(AuthException):
    def __init__(self):
        super().__init__('\nInvalid input. Please enter correctly!')
