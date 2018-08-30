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
		for line in f:
			Data = line.split(",")
			name = Data[0]
			email = Data[1]
			print("DB1: new entry for contact")	
			sleep(.1)
			del(Data)
			try:
				cur.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (?, ?);".\
					format(tn='table1', idf=column1, cn=column2), (name, email))
			except s.IntegrityError:
				print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
			
			
			c.commit()
			sleep(.1)
		#del(line)
f.close()
c.close()