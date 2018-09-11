import sqlite3 as s
from time import sleep
database = "/root/disk3/database_main.sqlite"
table1 = 'table1'
column3 = 'ip'
c = s.connect(database)
cur = c.cursor()

cur.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table1, cn=column3, ct=column_type))
