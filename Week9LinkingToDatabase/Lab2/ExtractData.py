# David Markham
# 19-11-2020
# Connect to a Database using Python 
# Get data where ID = 1.

# Import libraries. 
import mysql.connector
from mysql.connector import cursor

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database="datarepresentation" 
) 
# Get data where ID is 1.
cursor = db.cursor()
sql = "select * from student where id = %s"
values = (1,)

cursor.execute(sql, values) 
result = cursor.fetchall()
for x in result:
    print(x) 