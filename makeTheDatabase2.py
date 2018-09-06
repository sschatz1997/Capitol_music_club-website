import sqlite3 as s
from time import sleep

database = "/root/disk3/password_main.sqlite"
table1 = 'user_db'
column1 = 'first_name'
column2 = 'last_name'
column3 = 'username'
column4 = 'password'
field_type = 'TEXT'
column_type = 'TEXT'
c = s.connect(database)
cur = c.cursor()

cur.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table1, nf=column1, ft=field_type))
	

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table1, cn=column2, ct=column_type))

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table1, cn=column3, ct=column_type))
cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table1, cn=column4, ct=column_type))

c.close()