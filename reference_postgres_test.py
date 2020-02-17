#!/usr/bin/python3
import psycopg2
try:
    connect_str = "dbname='testpython' user='ec2-user' host='localhost' password='sean'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE wes_test (name char(40));""")
    cursor.execute("""SELECT * from wes_test""")
    conn.commit() # <--- makes sure the change is shown in the database
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()
except Exception as e:
    print(e)
