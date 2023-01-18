import button
import printer
import mail
import time
import display
import sound

latest_email: mail.ReceivedMail = None
amount_unread: int = -1

def button_callback():
    global amount_unread
    print("Button pressed")

    if latest_email == None:
        print("No email available")
    else:
        with open("latest.txt", "w") as file:
            # Write subject and sender to text file
            file.write(f"Subject: {latest_email.subject}\n")
            file.write(f"From: {latest_email.sender}\n")
            body = latest_email.get_body_and_mark_read()
            if body != None:
                file.write(body)
        printer.print("latest.txt")
        amount_unread -= 1
        print(f"Printed latest email and marked it as read: {amount_unread}")

def main():
    global latest_email, amount_unread
    button.set_callback(button_callback)
    display.init()
    sound.init()
    while True:
        unread_indexes = mail.get_unread_indexes()
        if (amount_unread != len(unread_indexes)):
            amount_unread = len(unread_indexes)
            if (amount_unread > 0):
                latest_email = mail.read_message_by_index(unread_indexes[-1])
            display.set_mail_info(latest_email, amount_unread)
            sound.play_effect()
        time.sleep(5)

if __name__ == "__main__":
    main()