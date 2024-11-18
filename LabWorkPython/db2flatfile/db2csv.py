import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

sqlSelect = "select * from avocados"
cur.execute(sqlSelect)
cols = [col[0] for col in cur.description]
print('Number of columns: ' + str(len(cols)))
recs = cur.fetchmany(5)
print ('Number of records: ' + str(len(recs)))

import csv
import io
outstring = io.StringIO()
writer = csv.writer(outstring, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(recs[0])
print(outstring.getvalue())

print ('Writing records...')
with open ('output.csv', 'w', newline = '\n') as file:
    csvwriter = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    for rec in recs:
        csvwriter.writerow(rec)

print(str(len(recs)) + ' records written to output.csv')