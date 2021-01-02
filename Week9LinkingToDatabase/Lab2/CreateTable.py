# David Markham
# 19-11-2020
# Connect to a Database using Python 
# Create table. 

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

sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

cursor.execute(sql) 