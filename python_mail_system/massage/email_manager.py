from massage.email_model import Email
from datastore.tables import get_emailes_db
from exceptions import *
from folder import FolderManager  


class EmailManager:

    email = Email
    emailes_db = get_emailes_db()

    @classmethod
    def make_massage(cls, subject, body, send_id, recip_id, folder_name):
        try:
            folder_id = FolderManager.make_folder(folder_name, send_id)
            email_instance = cls.email(
                subject, body, send_id, recip_id, f'{folder_id}')
            cls.emailes_db.insert(email_instance.dict_attributes())
        except EmptyFieldError as err:
            print(err)

    @classmethod
    def show_inbox(cls, user_id, folder_name):
        inbox = cls.emailes_db.join_all('subject, body, sender_id',
                                f"id = '{user_id}' and folder_name = '{folder_name}'")
        return inbox