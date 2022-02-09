# pip install mysql-connector

import mysql.connector as sqlcon

db = sqlcon.connect(host = "127.0.0.1", user = "root", passwd = "sahil@123", database = 'essential')

cur = db.cursor()

cur.execute("update student set mark = 89 where sname = 'Isha'")
cur.execute("select * from student")

for i in cur:
	print(i)

cur.close()
db.commit()