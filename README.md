# InnoVote
Voting backend using Google Forms and Google Sheets API

Instructions
 1. Create a Google Form using any trusted Google Account
 2. Enable Captcha on the form by copying the script from https://xfanatical.com/blog/captcha-for-forms/ into the script editor of the form
 3. Copy the code from the "duprem" file in the repo to the script editor of the Google Sheet containing form responses.
 4. Display the form responses on a Google Sheet
 5. Create a service account using Google API services(Tutorial:https://www.youtube.com/watch?v=cnPlKLEGR7E)
 6. Share the Google Sheet with the service account created
 7. Publish the form and begin accepting votes
 
Voting 
 1. Create an sqlite3 database containing fields for voterID, party voted for, and a boolean flag that is set to 1 once a vote is cast
 2. Once the voting period has elapsed, run "innovote.py" on the all the sheets created.
 3. Run "tally.py" to sum all the votes collected from the central database.
