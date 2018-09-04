import sqlite3 as s
from time import sleep

database = "/root/disk3/password_main.sqlite"
table1 = 'table2'
column1 = 'username'
column2 = 'password'
field_type = 'TEXT'
column_type = 'TEXT'
c = s.connect(database)
cur = c.cursor()

cur.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table1, nf=column1, ft=field_type))
	

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table1, cn=column2, ct=column_type))

c.commit()
c.close()