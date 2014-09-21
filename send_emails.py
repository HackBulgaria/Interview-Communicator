# -*- coding: utf-8 -*-
import smtplib
import json
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from settings import SMPT_SERVER, SMPT_SERVER_PORT, EMAIL, PASSWORD

json_data = open('people.json')
people = json.load(json_data)

server = smtplib.SMTP(SMPT_SERVER, SMPT_SERVER_PORT)
server.ehlo()
server.starttls()
server.login(EMAIL, PASSWORD)

for person in people:
    html = u"""\
        <html>
          <head></head>
          <body>
            <p>Здравей, {}</p>

            <p>Дойде време и за интервютата за Programing101 - курса към Хак България.</p>
            <p>
                <strong>
                    Датата и часът за твоето интервю са: {} - {}h.<br>
                    Молбата ни е да потвърдиш на този email, ако си ОК с датата и часa.
                </strong>
            </p>

            <p>Подготвили сме ти малко материали, които да прочетеш и решиш преди началото на курса: <a href="https://hackbulgaria.com/course/Prog101-2/#pre-reading">https://hackbulgaria.com/course/Prog101-2/#pre-reading</a>
            </p>
            Важното за интервютата е:
            <ul>
                <li>Интервюто ще се проведе по Skype.</li>
                <li>Продължителността на едно интервю е 15 минути.</li>
                <li>Skype акаунтът, който искаш да намериш е: <code>hackbulgaria</code>.</li>
                <li>Ще си поговорим с теб, за да разберем колко си мотивиран-а и до къде се простират знанията ти в областта на програмирането.</li>
            </ul>
            <p>
                Ако не използваш Skype ще се договорим за друга платформа.
            </p>
            <p>
                Поздрави,<br>
                Екипа на HackBulgaria
            </p>
          </body>
        </html>
        """.format(person['Name'], person['Date'], person['Hour'])

    you = person['Email']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "HackBulgaria дата и час за интервю."
    msg['From'] = EMAIL
    msg['To'] = you

    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    server.sendmail(EMAIL, you, msg.as_string())
    print("Send: " + you)

    time.sleep(4)

server.quit()
