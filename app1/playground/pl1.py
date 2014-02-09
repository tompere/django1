__author__ = 'mediaserver'

import sqlite3

db = sqlite3.connect('../db.sqlite3')
curs = db.cursor()
query = curs.execute('SELECT * FROM polls_poll')
for x in query.fetchall():
    print(x)
db.close()