import os
from time import sleep

os.system("cp viewcounter.php /var/www/html/viewcounter.php")
sleep(0.5)

os.system("cp index.html /var/www/html/index.html")
sleep(0.5)

os.system("cp styleSheet.css /var/www/html/styleSheet.css")
sleep(0.5)

os.system("cp formContact.php /var/www/html/formContact.php")
sleep(0.5)

os.system("cp contact.html /var/www/html/contact.html")
sleep(0.5)

os.system("cp blog.html /var/www/html/blog.html")
sleep(0.5)

os.system("cp Redirect.html /var/www/html/Redirect.html")
sleep(0.5)

print("Website updated")