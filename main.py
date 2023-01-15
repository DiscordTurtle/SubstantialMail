import button
import printer
import signal
import mail

def button_callback():
    print("Button pressed")

    latest = mail.get_last_unseen()
    with open("latest.txt", "w") as file:
        # Write subject and sender to text file
        file.write(f"Subject: {latest.subject}\n")
        file.write(f"From: {latest.sender}\n")
        file.write(latest.body)
    printer.print("latest.txt")

def main():
    button.set_callback(button_callback)
    signal.pause()
    mail.close()

if __name__ == "__main__":
    main()