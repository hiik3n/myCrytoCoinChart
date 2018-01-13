import sqlite3

conn = sqlite3.connect("RemitanoDB.db")

for _r in conn.execute("select * from records").fetchall():
    print(_r)

conn.close()