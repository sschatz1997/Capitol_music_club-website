import sqlite3 as s
from time import sleep

database = "/root/disk3/database.sqlite"
table1 = 'table1'
table2 = 'table2'
column1 = 'column1'
column2 = 'column2'
field_type = 'INTEGER'
c = s.connect(database)
cur = c.cursor()

cur.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table1, nf=column1, ft=field_type))

cur.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table2, nf=column1, ft=field_type))		