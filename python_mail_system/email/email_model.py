from datetime import datetime


class Email:

    def __init__(self, subject: str, body: str, email_id=None,
                 send_id=None, recip_id=None, folder_id=None, status=None):

        self.email_id = email_id
        self.send_id = send_id
        self.recip_id = recip_id
        self.folder_id = folder_id
        self.subject = subject
        self.body = body
        self.time_stamp = datetime.now()
        self.status = status

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if not value:
            raise EmptyFieldError
        self._subject = value

    @property
    def body(self):
        return self._body

    @subject.body
    def body(self, value):
        if not value:
            raise EmptyFieldError
        self._body = value

    def dict_attributes(self):
        return {
            'subject': self.subject,
            'body': self.body,
            'sender_id': self.send_id,
            'recipient_id': self.recip_id,
            'folder_id': self.foder_id,
            'time_stamp': self.time_stamp,
        }
