import gspread
import sqlite3
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)

sheet = client.open("InnoVote1").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

connection = sqlite3.connect("voterlist.db")
cursor = connection.cursor()

for i in range(len(data)):
    val = list(data[i].values())[1:3]
    print(val)
    format_str = """UPDATE voterlist SET vote = '{party}', voted = 1 WHERE id = '{voterid}' AND voted = 0;"""
    sql_command = format_str.format(party=val[1], voterid=val[0])
    print(sql_command)
    cursor.execute(sql_command)

connection.commit()
connection.close()
