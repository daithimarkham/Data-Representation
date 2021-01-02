# David Markham
# 19-11-2020
# Connect to a Database using Python 
# Update dat in table.

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
sql = "update student set name = %s, age = %s where id = %s"
values = ("Joe", 33, 4) 

cursor.execute(sql, values) 
db.commit()
print("Update done.") 