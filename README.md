Interview-Communicator
======================

A set of rules and scripts for making interviews for Hack Bulgaria's courses

## TL; DR

You can send emails, if you have proper `people.json` and `settings.py` file, by running:

```
$ python send_emails.py start
```

Where `start` is a filename, placede in the `messages/` folder - this is the template of the message that is going to be sent to every person from `people.json`

## Steps for making interview schedule with students.

0. Edit `settings.py` with your email credentials. Don't fotget to change the title of the email
1. From your table, somewhere, export a CSV file with the interview schedule.
2. Transform it to JSON. You can use http://www.convertcsv.com/csv-to-json.htm
3. Make sure that the fields, that you use in your email template, like `{Date}`, are present in the JSON file.
4. You need Python v. > 3
5. Execute `python send_emails.py <name_of_template_located_in_messages/_folder>`

### settings.py

There is an `example_settings.py` file. You can rename it to `settings.py` and insert your email credentials and the desired SMTP server.

Here is an example for Google:

```python
EMAIL = 'your-email-here@gmail.com'
PASSWORD = "your-password-here"
SMPT_SERVER = 'smtp.gmail.com'
SMPT_SERVER_PORT = 587
```

## Testing an email

You can rename `example_people.json` to `people.json` and send RadoRado or yourself an email to test if everything is correct, before running the script on live data.
