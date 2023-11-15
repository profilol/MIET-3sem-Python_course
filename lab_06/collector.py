import email
import time
from email.header import decode_header
from imaplib import IMAP4_SSL
import os
from dotenv import load_dotenv
import re

load_dotenv("./config.env")

imap_host = os.getenv('IMAP_HOST')
imap_port = os.getenv('IMAP_PORT')

valid_email = os.getenv('EMAIL_LOGIN')
valid_password = os.getenv('EMAIL_PASSWORD')

refresh_time = float(os.getenv('PERIOD_CHECK'))

with IMAP4_SSL(imap_host, int(imap_port)) as M:
    rc, resp = M.login(valid_email, valid_password)
    while True:
        M.select()
        typ, data = M.search(None, 'UNSEEN')
        for num in data[0].split():
            typ, msg = M.fetch(num, '(RFC822)')
            obtained_msg = email.message_from_bytes(msg[0][1])
            header = decode_header(obtained_msg["Subject"])[0][0]

            print(header)

            if re.search("[[Ticket#\d]*[] Mailer]", header) is not None:
                with open("./success_request.log", "a") as log_file:
                    log_file.write(f"ID:{obtained_msg['Message-ID']} TEXT:{obtained_msg.get_payload()}")
            else:
                with open("./error_request.log", "a") as log_file:
                    log_file.write(obtained_msg.get_payload())
        time.sleep(refresh_time)