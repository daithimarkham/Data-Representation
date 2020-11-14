# David Markham
# 11-12-2020 

# Implementing a Rest Server/ How to write an application server.

# REQUIREMENTS
# 1. An app server that has a RESTful interface to provide CRUD operations for one database table.
# 2. pick something at random like a book, you should choose your own entity.
# - Book will have:
#       - An id (Integer, auto increment) KEY i.e. this will be the unique identifier.
#       - A title, An Author, A price (integer, the price in cent).
#       - There are other attributes it could have ISBN (this could have been the unique identifier).
#       - Can choose to use an ID instead to make this as general as possible.

  
from flask import Flask, url_for, request, redirect, abort, jsonify 

app = Flask(__name__, static_url_path='', static_folder='staticpages')

books=[
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
    {"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
    {"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}
]
nextId=4

@app.route('/') # Map to url.
def index():
    return "hello"
# GET all
@app.route('/books')
def getAll():
    return jsonify(books)
# Find By id
@app.route('/books/<int:id>') # map url
def findById(id): # function
    foundBooks = list(filter (lambda t : t["id"]== id, books)) # Search through array of books and return id where equal to books.
    if len(foundBooks) == 0: # Setting responses if length of books is zero, find nothing, 
        return jsonify({}) , 204 # return 
    return jsonify(foundBooks[0]) # if two books have same id, return first book.

# CREATE
# Curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create(): # function to send back requests.
    global nextId
    if not request.json: # if no json in request
        abort(400)
    
    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    books.append(book)
    nextId += 1
    return jsonify(book)


    return "served by Create "

# Update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    return jsonify(currentBook)

# Delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)



