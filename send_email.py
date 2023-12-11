import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()
my_email = os.getenv("MY_EMAIL")
password_email = os.getenv("API_GOOGLE")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = my_email
    password = password_email

    receiver = my_email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
