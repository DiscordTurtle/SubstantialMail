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
    body: str

def get_last_unseen() -> ReceivedMail:
    status, count = imap.select("INBOX")
    status, message_nums = imap.search(None, "UNSEEN")

    messages = re.findall(r"\d+", str(message_nums))

    amount_unread = len(messages)
    newest_unread = messages[-1]

    status, message = imap.fetch(str(newest_unread), "(RFC822)")
    print(message)
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

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if msg.get_content_type() == "text/plain" and "attachment" not in part.get("Content-Disposition"):
                    body = part.get_payload(decode=True).decode()
        else:
            if msg.get_content_type() == "text/plain":
                body = msg.get_payload(decode=True).decode()
        return ReceivedMail(sender, subject, body)

def set_last_as_read():
    pass

def close():
    imap.close()
    imap.logout()