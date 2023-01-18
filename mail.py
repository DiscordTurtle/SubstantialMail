import imaplib
import email
from dataclasses import dataclass
from email.header import decode_header
import re

USERNAME = "substantialmail@gmail.com"
PASSWORD = "bowxqkamcinneykp"
IMAP_SERVER = "imap.gmail.com"

imap = imaplib.IMAP4_SSL(IMAP_SERVER)
imap.login(USERNAME, PASSWORD)

@dataclass
class ReceivedMail:
    sender: str
    subject: str
    _index: int
    _body: str

    def get_body_and_mark_read(self) -> str:
        if self._body == None:
            status, message = imap.fetch(str(self._index),'(RFC822)')

            response = message[0]
            msg = email.message_from_bytes(response[1])
            if msg.is_multipart():
                for part in msg.walk():
                    if msg.get_content_type() == "text/plain" and "attachment" not in part.get("Content-Disposition"):
                        self._body = part.get_payload(decode=True).decode()
            else:
                if msg.get_content_type() == "text/plain":
                    self._body = msg.get_payload(decode=True).decode()
        return self._body
    

def get_unread_indexes() -> list:
    status, count = imap.select("INBOX")
    status, message_nums = imap.search(None, "UNSEEN")

    return re.findall(r"\d+", str(message_nums))

def read_message_by_index(index) -> ReceivedMail:
    status, message = imap.fetch(str(index),'(BODY.PEEK[])')
    if (len(message) <= 0):
        return None
    else:
        response = message[0]
        # parse a bytes email into a message object
        msg = email.message_from_bytes(response[1])

        # decode the email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding)

        # decode email sender
        sender, encoding = decode_header(msg.get("From"))[0]
        if isinstance(sender, bytes):
            sender = sender.decode(encoding)
            
        return ReceivedMail(sender, subject, index, None)

def close():
    imap.close()
    imap.logout()