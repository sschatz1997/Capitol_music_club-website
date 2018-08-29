from time import sleep 

contactsMain = "/var/www/html/contact.txt"
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

with open(contactsMain, "r") as f:
	while True:
		for line in f:
			Data = line.split(",")
			name = Data[1]
			email = Data[2]
			print(name, " ", email)	
			sleep(.1)
			del(Data)
			if Data == "":
				False
