from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase


db_connector = PostgreSQLDatabase(
    dbname='postgres', user='postgres', password='1234')


# users table

users_db = DatabaseHandler('users', db_connector)

users_db.create_table({
    'id': 'bigserial primary key',
    'name': 'VARCHAR(50)',
    'username': 'VARCHAR(50)',
    'salt': 'TEXT NOT NULL',
    'password': 'TEXT NOT NULL',
    'logging': 'BOOLEAN DEFAULT false'
})

def get_users_db():
    return users_db

# folders table

folders_db = DatabaseHandler('folders', db_connector)

folders_db.create_table({
    'folder_id': 'BIGSERIAL PRIMARY KEY',
    'folder_name': 'VARCHAR(50) NOT NULL',
    'user_id': 'INTEGER NOT NULL REFERENCES users(id)',
    'time_stamp': 'TIMESTAMP DEFAULT NOW()',
})

def get_folders_db():
    return folders_db


# emailes table

emailes_db = DatabaseHandler('emails', db_connector)

emailes_db.create_table({
    'email_id': 'BIGSERIAL PRIMARY KEY',
    'subject': 'VARCHAR(200) NOT NULL',
    'body': 'TEXT NOT NULL',
    'sender_id': 'INTEGER NOT NULL REFERENCES users(id)',
    'ecipient_id': 'INTEGER NOT NULL REFERENCES users(id)',
    'folder_id': 'INTEGER NOT NULL REFERENCES folders(folder_id)',
    'time_stamp': 'TIMESTAMP DEFAULT NOW()',
    'status': "VARCHAR(20) NOT NULL DEFAULT 'unread' "
})

def get_emailes_db():
    return emailes_db


# user_folder table

user_folder = DatabaseHandler('user_folder', db_connector)

user_folder.create_table({
    'user_id': 'INTEGER NOT NULL REFERENCES users(id)',
    'folder_id': 'INTEGER NOT NULL REFERENCES folders(folder_id)',
    'PRIMARY KEY': '(user_id, folder_id)',
})