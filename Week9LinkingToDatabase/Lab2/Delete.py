# David Markham
# 19-11-2020
# Connect to a Database using Python 
# Delete data in table.

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
sql = "delete from student where id = %s"
values = (1,) 

cursor.execute(sql, values) 
db.commit()
print("Delete done.") 