import smtplib
import json
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from settings import SMPT_SERVER, SMPT_SERVER_PORT, EMAIL, PASSWORD, SUBJECT

from copy import deepcopy

json_data = open('people.json')
people = json.load(json_data)

server = smtplib.SMTP(SMPT_SERVER, SMPT_SERVER_PORT)
server.ehlo()
server.starttls()
server.login(EMAIL, PASSWORD)

email_message = open('EMAIL_MESSAGE').read()

for person in people:
    html = deepcopy(email_message).format(
        person['Name'].strip(),
        person['Date'].strip(),
        person['Hour']).strip()

    # White spaces at the end.
    you = person['Email'].strip()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL
    msg['To'] = you

    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    server.sendmail(EMAIL, you, msg.as_string())
    print("Send: " + you)

    time.sleep(4)

server.quit()
