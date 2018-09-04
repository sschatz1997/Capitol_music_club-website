import time
import sqlite3 as s
import base64
from time import sleep 

contactsMain = "/var/www/html/contact.txt"
database = "/root/disk3/database_main.sqlite"
username_passwordMain = "/var/www/html/pass.txt"
database2 = "/root/disk3/password_main.sqlite"
errorLog = "/root/disk3/errorLog.txt"
table1 = 'table1'
column1 = 'name'
column2 = 'email'

table2 = 'table2'
column3 = 'username'
column4 = 'password'
#field_type = 'INTEGER'
column_type = 'TEXT'
c = s.connect(database)
x1 = s.connect(database2)
cur = c.cursor()
cur2 = x1.cursor()
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain, "r") as f:
	with open(username_passwordMain, "r") as f2:
	
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
				
				deleteData1 = open(contactsMain, "w")
				deleteData1.write(Data)
				deleteData1.close()
				c.commit()
				sleep(.1)
				
			for line in f2:
				U = line.split(",")
				username = U[0]
				password = U[1]
				password = base64.b64encode(password.encode())

				print("DB2: new user")	
				sleep(.1)
				del(U)
				try:
					cur2.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (?, ?);".\
						format(tn='table2', idf=column3, cn=column4), (username, password))
				except s.IntegrityError:
					print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
			
				deleteData2 = open(username_passwordMain, "w")
				deleteData12.write(U)
				deleteData2.close()			
				decoded = base64.b64decode(password.decode())
				x1.commit()
				sleep(.1)
			#del(line)
			#deleteData1 = open(contactsMain, "w")
			#deleteData1.write(Data)
			#deleteData1.close()
			#deleteData2 = open(username_passwordMain, "w")
			#del U[0]
			#del U[1]
			#deleteData1.write(U)
			#deleteData2.close()
				
			
f.close()
c.close()
f2.close()
x1.close()
