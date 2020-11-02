import sqlite3
connection = sqlite3.connect("voterlist.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM voterlist")
result = cursor.fetchall() 
for r in result:
    print(r)

