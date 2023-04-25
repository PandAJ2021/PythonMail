from massage.email_model import Email
from datastore.tables import get_emailes_db
from exceptions import *


class EmailManager:

    email = Email
    emailes_db = get_emailes_db()

    @classmethod
    def make_massage(cls, subject, body, send_id, recip_id): #send_id comes from logging
        try:
            email_instance = cls.email(
                subject, body, send_id, recip_id )
            return cls.emailes_db.insert(email_instance.dict_attributes()) #massage_d
        except EmptyFieldError as err:
            print(err)

    @classmethod
    def show_inbox(cls, user_id , subject=None):
        condition = f"recipient_id = '{user_id}'"
        if subject:
            condition += f"and subject = '{subject}'"
        inbox = cls.emailes_db.join_all('subject,email_time , body, sender_id ',condition)
        return inbox

    @classmethod
    def show_sentbox(cls, user_id , subject=None):
        condition = f"sender_id = '{user_id}'"
        if subject:
            condition += f"and subject = '{subject}'"
        inbox = cls.emailes_db.join_all('subject,email_time , body, recipient_id ',condition)
        return inbox
   
    @classmethod
    def send_massage(cls , massage_id ,username):
        pass
