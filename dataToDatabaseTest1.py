from time import sleep 
import sqlite3 as s

contactsMain = "/var/www/html/contact.txt"
database = "/root/disk3/database_main.sqlite"
table1 = 'table1'
column1 = 'name'
column2 = 'email'
field_type = 'INTEGER'
column_type = 'TEXT'
c = s.connect(database)
cur = c.cursor()

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain, "r") as f:
	while True:
		line = f.readlines(array[1])
		print(line)
		try:
			cur.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test');".\
				format(tn='table1', idf='column1', cn='column2'), ('test1', 'test2'))
		except s.IntegrityError:
			print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
		
		
		cur.commit()
		sleep(.1)
		#del(line)
f.close()
cur.close()