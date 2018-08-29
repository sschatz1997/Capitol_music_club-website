from time import sleep 
import sqlite3 as s

c = s.connect('test.db')
cur = con.cursor()
contactsMain = "/var/www/html/contact.txt"
database = "/root/disk3/database.db"
table1 = 'table1'
column1 = 'column1'

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain, "r") as f:
	while True:
		line = f.readlines(array[1])
		print(line)
			try:
				cin.excute("INSERT INTO {tn} {cn}VALUES (123456, 'test')".\
					format(tn=table_name, idf=id_column, cn=column_name))
			except s.IntegrityError:
				print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
		c.commit()
		sleep(.1)
		#del(line)
		c.close()
f.close()