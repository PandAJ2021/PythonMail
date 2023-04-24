from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
from user.user_manager import UserManager



# UserManager.register_user('mohammad jalili', 'MJ25757j-i', 'Mj12345678')
# UserManager.register_user('ali jalili', 'AJ25757j-i', 'AJ12345678' ,True)
# a = UserManager.authentication('mohammad jalili', 'Mj235757j-i', 'Mj12345678')
# print(a)

# a= UserManager.auth_pass('MJ25757j-i', 'Mj2345678')
# print(a)
a = UserManager.logging_user('MJ25757j-i', 'Mj12345678')

print(a.id)

# a = UserManager.get_id('MJ25757j-i')
# print(a)