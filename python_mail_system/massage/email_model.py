from datetime import datetime


class Email:

    def __init__(self, subject: str, body: str, send_id=None,
                recip_id=None, status=None, email_id=None):

        self.email_id = email_id
        self.send_id = send_id
        self.recip_id = recip_id
        self.subject = subject
        self.body = body
        self.time_stamp = datetime.now()
        self.status = status

    def dict_attributes(self):
        return {
            'subject': f"'{self.subject}'",
            'body': f"'{self.body}'",
            'sender_id': f'{self.send_id}',
            'recipient_id': f'{self.recip_id}',
        }

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

    @body.setter
    def body(self, value):
        if not value:
            raise EmptyFieldError
        self._body = value
