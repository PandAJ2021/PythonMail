from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase


db_connector = PostgreSQLDatabase(
    dbname='postgres', user='postgres', password='1234')


# users table

users_db = DatabaseHandler('users', db_connector)

users_db.create_table({
    'user_id': 'bigserial primary key',
    'name': 'VARCHAR(50)',
    'username': 'VARCHAR(50)',
    'salt': 'TEXT NOT NULL',
    'password': 'TEXT NOT NULL',
    'logging': 'BOOLEAN DEFAULT false'
})

def get_users_db():
    return users_db

# emailes table

emailes_db = DatabaseHandler('emailes', db_connector)

emailes_db.create_table({
    'email_id': 'BIGSERIAL PRIMARY KEY',
    'subject': 'VARCHAR(200) NOT NULL',
    'body': 'TEXT NOT NULL',
    'sender_id': 'INTEGER NOT NULL REFERENCES users(user_id)',
    'recipient_id': 'INTEGER NOT NULL REFERENCES users(user_id)',
    'email_time': 'TIMESTAMP DEFAULT NOW()',
    'read_status': "VARCHAR(20) NOT NULL DEFAULT 'unread' ",
    'sent_status' : "VARCHAR(20) NOT NULL DEFAULT 'draft' "
})

def get_emailes_db():
    return emailes_db