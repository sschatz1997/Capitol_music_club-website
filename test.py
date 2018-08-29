from time import sleep 

contactsMain = "/var/www/html/contact.txt"
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain, "r") as f:
	while True:
		line = f.readlines(array[1])
		print(line)
		name, email = line.split(',', 1)
	
		sleep(.1)
		del(line)
