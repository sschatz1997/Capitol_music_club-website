from time import sleep 
import sqlite3 as s

#c = s.connect('test.db')
contactsMain = "/var/www/html/contact.txt"
database = "/root/disk3/database.db"

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain) as f:
	while True:
		line = f.readlines(array[1])
		splitdata = line.split(";")
		print(splitdata)
		sleep(.1)
		#del(line)
f.close()