# setup database table for lab 
import pandas as pd
from pandas import DataFrame
import sqlite3

# create table in db
sql_create_table = """CREATE TABLE IF NOT EXISTS avocados ( 'Id' number,  'Date' text,  'AveragePrice' number,  'Total Volume' number,  '4046' number,  '4225' number,  '4770' number,  'Total Bags' number,  'Small Bags' number,  'Large Bags' number,  'XLarge Bags' number,  'Type' text,  'Year' number,  'Region' text  )"""
sql_drop_table = "DROP TABLE IF EXISTS avocados"
sql_count_recs = "SELECT COUNT(Id) from avocados"
con = sqlite3.connect("data.db")
c = con.cursor()
c.execute(sql_drop_table)
c.execute(sql_create_table)
con.commit()

# insert data from csv file to database
df = pd.read_csv('avocado.csv')
df.to_sql('avocados', con, if_exists='replace', index = False )
con.commit()

# check success
c.execute(sql_count_recs)
count = c.fetchone()[0]
if count > 0:
    print('database table "avocados" created')
    print('record count: ' + str(count))
con.close()