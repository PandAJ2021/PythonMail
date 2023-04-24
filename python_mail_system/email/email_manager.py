from email_model import Email
from datastore.tables import get_emailes_db
from exceptions import *


class EmailManager:

    email = Email
    emailes_db = get_emailes_db()

    @classmethod
    def make_massage(cls, subject, body, email_id, send_id, recip_id, folder_id):
        try:
            email_instance = cls.email(subject, body, email_id, send_id, recip_id, folder_id)
            emailes_db.insert(email_instance.dict_attributes())
        except EmptyFieldError as err:
            print(err)
    
