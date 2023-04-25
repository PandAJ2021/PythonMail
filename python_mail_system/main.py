from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
from user.user_manager import UserManager
from massage.email_manager import EmailManager

# from datetime import datetime
# datetime().
# UserManager.register_user('mohammad jalili', 'MJ25757j-i', 'Mj12345678')
# UserManager.register_user('ali jalili', 'AJ25757j-i', 'AJ12345678')
# a = UserManager.authentication('mohammad jalili', 'Mj235757j-i', 'Mj12345678')
# print(a)

# a= UserManager.auth_pass('MJ25757j-i', 'Mj2345678')
# print(a)
# a = UserManager.logging_user('MJ25757j-i', 'Mj12345678')

# print(a)

# a = UserManager.get_id('MJ25757j-i')
# print(a)

# EmailManager.make_massage('friendship', 'hello', '2','1' )
# a =EmailManager.make_massage('friendship', 'hi whats up', '1','2' )

# print(a)
# a= EmailManager.show_inbox('2')
# for i in a :
#     print(a[0][1].ctime())
# print(a)
b= EmailManager.show_sentbox('1')
print(b)

