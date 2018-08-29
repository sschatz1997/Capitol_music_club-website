import sqlite3

database = "/root/disk3/database.sqlite"
conn = sqlite3.connect(database)
c = conn.cursor()
c.execute("SELECT * FROM Posts")
print(c.fetchall())