import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

sqlSelect = "select * from avocados"
cur.execute(sqlSelect)
cols = [col[0] for col in cur.description]
print (cols)
record = cur.fetchone()
print(record)

sqlSelect = "select * from avocados where region = 'Tampa'"
cur.execute(sqlSelect)
rows = cur.fetchall()
print(len(rows))

sqlSelect = "select Date,AveragePrice, TotalVolume from avocados where region = 'Tampa'"
cur.execute(sqlSelect)
rows = cur.fetchone()
print([col[0] for col in cur.description])
print(rows)
print(len(rows))