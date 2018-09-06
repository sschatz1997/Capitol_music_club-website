import os
from time import sleep

os.system("git pull https://github.com/sschatz1997/Capitol_music_club-website")
sleep(2)

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

os.system("cp rap.html /var/www/html/rap.html")
sleep(0.5)

os.system("cp music.html /var/www/html/music.html")
sleep(0.5)

os.system("cp charts.html /var/www/html/charts.html")
sleep(0.5)

os.system("cp login.html /var/www/html/login.html")
sleep(0.5)

os.system("cp pass.php /var/www/html/pass.php")
sleep(0.5)

os.system("cp succes.html /var/www/html/succes.html")
sleep(0.5)

os.system("cp login.php /var/www/html/login.php")
sleep(0.5)
print("\n" + "Website updated")
