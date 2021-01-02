# David Markham
# 19-11-2020
# Connect to a Database using Python 

# Import libraries. 
import mysql.connector
from mysql.connector import cursor

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
) 

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation") 