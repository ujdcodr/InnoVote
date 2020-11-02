import sqlite3

vote_count = {'P1':0,'P2':0,'P3':0,'P4':0}
connection = sqlite3.connect("voterlist.db")
cursor = connection.cursor()

cursor.execute("SELECT vote FROM voterlist")
result = cursor.fetchall()
for r in result:
    if r[0] is not None:
        vote_count[r[0]]+=1

print(vote_count)
connection.close()


