from time import sleep 
import sqlite3 as s

c = s.connect('test.db')
cur = c.cursor()
contactsMain = "/var/www/html/contact.txt"
database = "/root/disk3/database.db"
table1 = 'table1'
column1 = 'column1'
column2 = 'column2'

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain, "r") as f:
	while True:
		line = f.readlines(array[1])
		print(line)
		try:
			c.execute("INSERT INTO {tn} {cn}VALUES (123456, 'test')".\
				format(tn=table1, idf=column1, cn=column_name))
		except s.IntegrityError:
			print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
		c.commit()
		sleep(.1)
		#del(line)
		c.close()
f.close()