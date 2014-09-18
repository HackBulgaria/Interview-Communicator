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
