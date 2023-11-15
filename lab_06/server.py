import socket
import os
from email.message import EmailMessage

from dotenv import load_dotenv
from smtplib import SMTP


def send_message_to_email(mail, mail_password, message: EmailMessage):
    smtp_mail = os.getenv('SMTP_HOST')
    smtp_port = os.getenv('SMTP_PORT')

    with SMTP(f"{smtp_mail}:{smtp_port}") as smtp:
        smtp.starttls()
        smtp.login(mail, mail_password)
        smtp.send_message(message)


def create_message(status, message, message_id):
    part_message = message.split("message = ")[1]
    created_message = EmailMessage()
    created_message['From'] = valid_email
    created_message['To'] = valid_email
    if status == "OK":
        created_message['Subject'] = f"[Ticket#{message_id}] Mailer"
        created_message.set_content(part_message)
    else:
        created_message['Subject'] = f"Error Mailer"
        created_message.set_content(part_message)
    print(created_message)
    message_id += 1
    return created_message


host = '127.0.0.1'
port = 25565
message_id = 12345

load_dotenv("./config.env")

valid_email = os.getenv('EMAIL_LOGIN')
valid_password = os.getenv('EMAIL_PASSWORD')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen(1)
    connection, address = sock.accept()

    with connection:
        print(f"Connected by {address}")
        while True:
            response = connection.recv(1024)
            if not response:
                break
            if response:
                print(f"Received message = {repr(response)}")
            response_message = response

            decoded_message = response_message.decode('UTF-8')

            status = "OK"
            if decoded_message.find(f"address = {valid_email}") == -1 or decoded_message.find(
                    f"password = {valid_password}") == -1:
                status = "Incorrect mail or password"

            message_for_mail = create_message(status, decoded_message, message_id)

            send_message_to_email(valid_email, valid_password, message_for_mail)

            connection.sendall(bytes(status, 'UTF-8'))
