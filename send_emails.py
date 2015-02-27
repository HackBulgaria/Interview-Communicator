import smtplib
import json
import time
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from settings import SMPT_SERVER, SMPT_SERVER_PORT, EMAIL, PASSWORD, SUBJECT, TIMEOUT

from copy import deepcopy

from random import randint

if len(sys.argv) < 2:
    print("No message given. You should give the filename of the message, located in messages/ folder, that you want to send")
    print("For example: python send_emails.py NODE_ONLINE")
    sys.exit()


json_data = open('people.json')
people = json.load(json_data)

server = smtplib.SMTP(SMPT_SERVER, SMPT_SERVER_PORT)
server.ehlo()
server.starttls()
server.login(EMAIL, PASSWORD)


email_message = open('messages/{}'.format(sys.argv[1])).read()
print(email_message)

for person in people:
    person = {key: value.strip() for key, value in person.items()}

    html = deepcopy(email_message).format(**person)

    # White spaces at the end.
    you = person['Email']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL
    msg['To'] = you

    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    server.sendmail(EMAIL, you, msg.as_string())
    print("Send: " + you)

    time.sleep(randint(TIMEOUT, TIMEOUT + 5))

server.quit()
