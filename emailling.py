import smtplib
import imghdr
from email.message import EmailMessage
import os


def send_email(image_path):
    host = "smtp.gmail.com"
    port = 587

    username = "momo9211654@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "momo9211654@gmail.com"

    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP(host, port)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()
    print("Email was sent!")
