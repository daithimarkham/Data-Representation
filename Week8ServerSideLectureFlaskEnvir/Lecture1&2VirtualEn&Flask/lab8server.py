# David Markham 
# 12-11-2020
# Create a server for the virtual environment. 
# Basics of as Flask server
# More info in Doc For Flask


# Import Flask 
from flask import Flask, url_for, request, redirect, abort

# Create Flask app
app = Flask(__name__, static_url_path='', static_folder='staticpages') 

@app.route('/') # Map to url. Redirect to url for login. 
def index():
   return  redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    return "served by Login"

@app.route('/user') # Map User, enter user at end of url and will display content below. 
def getUser(): # Method is GET
    return "served by getUser"

@app.route('/user/<int:id>') # Find user by ID
def findByIdUser(id):
    return "served by findByIdUser with id = "+str(id)

@app.route('/user', methods=['POST']) # Map POST method, posts method. Can't check on browser. 
def createUser(): # Need to use Flask, cause post method. curl -X POST http://127.0.0.1:5000/user 
    return "served by createUser"

@app.route("/demo_url_for") # Demo url finds user ID
def demoUrlFor():
    returnString = "url For index is "+ url_for('index')
    returnString += "<br/>"
    returnString += "url for findByIdUser "+ url_for('findByIdUser', id=12)
    return returnString

# Map route for demo request 
@app.route("/demo_request", methods=['POST', 'GET', 'DELETE']) 
def demoRequest():
    return request.method 

#  Run Flask
if __name__ == "__main__":
    print("in if")
    app.run(debug=True) 