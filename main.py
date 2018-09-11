import time
import sqlite3 as s
import base64
from time import sleep 
import sys

contactsMain = "/var/www/html/contact.txt"
database = "/root/disk3/database_main.sqlite"
username_passwordMain = "/var/www/html/pass.txt"
database2 = "/root/disk3/password_main.sqlite"
errorLog = "/root/disk3/errorLog.txt"
ip = "/var/www/html/ip.txt"

table1 = 'table1'
column1 = 'name'
column2 = 'email'
column7 = 'ip'

table2 = 'user_db'
column3 = 'first_name'
column4 = 'last_name'
column5 = 'username'
column6 = 'password'
#field_type = 'INTEGER'
column_type = 'TEXT'

c = s.connect(database)
x1 = s.connect(database2)
cur = c.cursor()
cur2 = x1.cursor()
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(ip, "r+") as f0:
	with open(contactsMain, "r+") as f:
		with open(username_passwordMain, "r+") as f2:
		
			while True:
				for line in f:
					Data = line.split(",")
					name = Data[0]
					email = Data[1]
					print("DB1: new entry for contact")	
					sleep(.1)
					del(Data)
					for line in f0:
						ip = f0.readline()
					try:
						cur.execute("INSERT INTO {tn} ({idf}, {cn}, {cn2}) VALUES (?, ?, ?);".\
							format(tn='table1', idf=column1, cn=column2, cn2=column7), (name, email, ip))
					except s.IntegrityError:
						print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
					

					c.commit()
					sleep(.1)
					del(line)
				
					
				for line in f2:
					U = line.split(",")
					print(U)
					first_name = U[0]
					last_name = U[1]
					username = U[2]
					password = U[3]
					password = base64.b64encode(password.encode())

					print("DB2: new user")	
					sleep(.1)
					del(U)
					try:
						cur2.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (?, ?);".\
							format(tn=table2, idf=column3, cn=column4), (first_name, last_name))
					except s.IntegrityError:
						print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
					x1.commit()
					try:
						cur2.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (?, ?);".\
							format(tn=table2, idf=column5, cn=column6), (username, password))				
					except s.IntegrityError:
						print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))	
					x1.commit()
					sleep(.1)
					del(line)
					print(u, Data)
					#f.truncate(0)
					#f2.truncate(0)
f0.close()
f.close()
f2.close()
f.close()
c.close()
x1.close()
