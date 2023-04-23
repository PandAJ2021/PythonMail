from user.user_model import User

class UserManager:

    def __init__(self , user = User):
        self.user = user    
        self.register = False

    def register_user(self,full_name: str, username: str, password: str ):
        
        try:
            instance = self.user(full_name , username , password)
        except Exception as err:
            print(err)


test= User('Ali Jalili', 'Li23582_d', '12345aaL')
print(test.__dict__)