# InnoVote
Voting backend using Google Forms and Google Sheets API <br/>
Demo Link: https://youtu.be/CoaJ8Z6U_F0
<br/>
The following technologies make up InnoVote's procedural pipeline:
* Google Forms - Single point of data collection from voters
* Google Sheets - Consolidated view of voter responses
* Google Apps Script - Implementation of form CAPTCHA and duplicate vote removal
* Google Developer Console - Service account creation to enable API calls
* Google Sheets API - Enable backend voter verification and vote tally

InnoVote’s  backend is programmed in Python and makes use of the following packages:
* gspread - Google Sheet data collection
* sqlite3 - SQL database creation
* oauth2client.service_account - Security


Set up
1. Create a Google Form using any trusted Google Account
2. Enable Captcha on the form by copying the script from https://xfanatical.com/blog/captcha-for-forms/ into the script editor of the form
3. Copy the code from the "duprem" file in the repo to the script editor of the Google Sheet containing form responses.
4. Configure a time driven trigger on the Google Sheet’s Apps Script page to call the duplicate removal macro every minute.
5. Display the form responses on a Google Sheet
6. Create a service account using GoogleAPI services. Download the JSON key produced at the end. This key must be kept in a secure location.
(Tutorial:https://www.youtube.com/watch?v=cnPlKLEGR7E)
7.Share the Google Sheet with the service account created
8. Publish the form and begin accepting votes

Voting
1. Create an sqlite3 database containing fields for voterID, party voted for, and a boolean flag that is set to 1 once a vote is cast
2. Once the voting period has elapsed, run "innovote.py" on all the sheets created, using the JSON key from step 6.
3. Run "tally.py" to sum all the votes collected from the central database.

For detailed instructions on enabling CAPTCHA, removing duplicate entries and setting up a Google service account, refer the InnoVote Support document.
