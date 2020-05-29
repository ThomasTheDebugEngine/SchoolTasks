import sqlite3
conn = sqlite3.connect('temporary.db')
c = conn.cursor()
c.execute("SELECT * from table_name where id=cust_id") for row in c:
