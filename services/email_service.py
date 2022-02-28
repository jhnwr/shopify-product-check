import os
import smtplib
import ssl

from dotenv import load_dotenv

load_dotenv()


def send_mail(items):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv("shipfromemail")
    receiver_email = os.getenv("shiptoemail")
    password = os.getenv("emailpass")
    body = '\n'.join([f'{item[0], item[4]}' for item in items])
    print(items)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, body)


if __name__ == '__main__':
    send_mail()
