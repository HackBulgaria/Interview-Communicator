Interview-Communicator
======================

A set of rules and scripts for making interviews for Hack Bulgaria's courses

## Steps for making interview schedule with students.

1. Download all people from F6S as a CSV file.
2. Import that CSV file into a Google Documents Spreadsheet
3. Trim the data and make it have 4 columns:
    - Name
    - Email
    - Date
    - Hour
4. Export the data as CSV file again.
5. Transform it to a JSON file (You can do that with http://www.convertcsv.com/csv-to-json.htm)
6. Save the file as `people.json`
7. Run the script `send_emails.py` - requires Python v. > 3

## Detailed explanation

Starting from step 5, you can see `example_people.json` for the required format of the JSON file.

Once you have the JSON file, you will have to take care of the following files:

### settings.py

There is an `example_settings.py` file. You can rename it to `settings.py` and insert your email credentials and the desired SMTP server.

Here is an example for Google:

```python
EMAIL = 'your-email-here@gmail.com'
PASSWORD = "your-password-here"
SMPT_SERVER = 'smtp.gmail.com'
SMPT_SERVER_PORT = 587
```

### Email messages and running the Script

In order to send an email, you have to create `messages` folder (which is in `.gitignore`).

`send_emails.py` will look inside that folder for the given message.

In order to run the script, you have to pass the email body filename, which you have created in `messages/` folder.

For example, if we have `messages/NODE_ONLINE` file, in order to run the script, you will have to do the following:

```
python send_emails NODE_ONLINE
```

There is an `example_EMAIL_MESSAGE` which contains the email body.

Change it accordingly but **do not remove the `{}` placeholders** from the string.

### people.json

If you rename `example_people.json` to `people.json` you can test if the script is working for you.

You will send email to me, but it is a better idea to send email to yourself, in order to have quick feedback loop.
