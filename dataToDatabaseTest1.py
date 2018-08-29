from time import sleep as s
import sqlite3 as s

c = s.connect('test.db')
contactsMain = "/var/www/html/contact.txt"
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain) as f:
	while 0 != 10:
		line = f.readlines(array[i])
		print(line)
		s(.1)
		i += 1
f.close()