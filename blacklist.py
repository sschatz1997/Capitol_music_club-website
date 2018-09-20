import sqlite3 as s
from time import sleep

database = "/root/disk3/blacklist.sqlite"
table1 = 'blacklist'
column1 = 'ip'
column2 = 'email'
field_type = 'TEXT'
column_type = 'TEXT'
c = s.connect(database)
cur = c.cursor()

cur.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table1, nf=column1, ft=field_type))
	

c.commit()
c.close()