import psycopg2
import sys
from config import *

con = None

try:

    con = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'"
                           % (DB_POSTGRES_HOST, DB_POSTGRES_NAME, DB_POSTGRES_USER, DB_POSTGRES_PWD))

    cur = con.cursor()

    # cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    # cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    # cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    # cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    # cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    # cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    # cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    # cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    # cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
    #
    # con.commit()
    cur.execute("SELECT * FROM t01")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    print('Connect')

except Exception as e:

    print('Except')

    if con:
        con.rollback()

    print('Error %s' % e)
    sys.exit(1)


finally:

    if con:
        con.close()
        print('Close')