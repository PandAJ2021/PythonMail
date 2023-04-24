from email_model import Email
from datastore.database_manager import DatabaseHandler
from utils.database_connector import PostgreSQLDatabase
from exceptions import *


class EmailManager:
    email = Email

    def make_massage(cls):
        pass