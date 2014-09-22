Interview-Communicator
======================

A set of rules and scripts for making interviews for Hack Bulgaria's courses

## Steps for making interview schedule with studensts.

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

### EMAIL_MESSAGE

There is an `example_EMAIL_MESSAGE` which contains the email body.

You will have to rename it to `EMAIL_MESSAGE`.

Change it accordingly but **do not remove the `{}` placeholders** from the string.
They are in a particular order - Name, Date, Hour

### people.json

If you rename `example_people.json` to `people.json` you can test if the script is working for you.

You will send email to me, but it is a better idea to send email to yourself, in order to have quick feedback loop.
