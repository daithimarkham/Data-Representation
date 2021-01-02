# David Markham
# 19-11-2020
# Connect to a Database using Python 
# Insert data into table.

# Import libraries. 
import mysql.connector
from mysql.connector import cursor

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database="datarepresentation" 
) 

cursor = db.cursor()

sql="insert into student (name, age) values (%s, %s)"
values = ("Mary",21)

cursor.execute(sql, values) 

db.commit()
print("1 record inserted, ID:", cursor.lastrowid) 