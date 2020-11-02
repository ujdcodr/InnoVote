import sqlite3

connection = sqlite3.connect("voterlist.db")
cursor = connection.cursor()

sql_command = """
CREATE TABLE voterlist ( 
id VARCHAR(20) PRIMARY KEY, 
voted INTEGER, 
vote VARCHAR(30));"""

cursor.execute(sql_command)

for i in range(1,4):
    format_str = """INSERT INTO voterlist (id,voted,vote)
    VALUES ("{voterid}","{voted}",NULL);"""
    sql_command = format_str.format(voterid="V"+str(i),voted=0)
    cursor.execute(sql_command)

connection.commit()

connection.close()
