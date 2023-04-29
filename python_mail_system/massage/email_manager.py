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
        inbox = cls.emailes_db.join_all('sender_id , subject, body ,email_time, read_status',condition)
        return inbox

    @classmethod
    def show_sentbox(cls, user_id , subject=None):
        condition = f"sender_id = '{user_id}'"
        if subject:
            condition += f"and subject = '{subject}'"
        inbox = cls.emailes_db.join_all('recipient_id , subject, body ,email_time',condition)
        return inbox
   
    @classmethod
    def send_massage(cls , email_id):
        cls.emailes_db.update({'sent_status': "'sent'"}, f"email_id = '{email_id}'")


    @classmethod
    def show_draft(cls , user_id , subject=None):
        condition = f"sender_id = '{user_id}' and sent_status = 'sent' "
        if subject:
            condition += f"and subject = '{subject}'"
        inbox = cls.emailes_db.join_all('recipient_id , subject, body ,email_time',condition)
        return inbox