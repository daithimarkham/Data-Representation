# David Markham
# 19-11-2020
# Here we put all the previous snippets of code in one program.

import mysql.connector
from mysql.connector import cursor

class BookDao:
    db = "" # Variable
    def __init__(self): # Create function 
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='datarepresentation'
        )
        #print ("connection made")

    def create(self, book): # CREATE function.
        cursor = self.db.cursor()
        sql = "insert into books (ISBN, title, author, price) values (%s,%s,%s,%s)"
        values = [ # Values passed into function.
            book['ISBN'],
            book['title'],
            book['author'],
            book['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self): # GETALL function
        cursor = self.db.cursor()
        sql = 'select * from books'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, ISBN): # Find all where ISBN = values.
        cursor = self.db.cursor()
        sql = 'select * from books where ISBN = %s'
        values = [ ISBN ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, book): # UPDATE book 
       cursor = self.db.cursor()
       sql = "update books set title = %s, author = %s, price = %s where ISBN = %s"
       values = [
           book['title'],
           book['author'],
           book['price'],
           book['ISBN']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return book

    def delete(self, ISBN):
       cursor = self.db.cursor()
       sql = 'delete from books where ISBN = %s'
       values = [ISBN]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['ISBN','title', 'author', 'price']
        book = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                book[colName] = value
        return book

bookDao = BookDao() 