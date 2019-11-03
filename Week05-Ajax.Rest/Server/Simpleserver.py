#!flask/bin/python
from flask import Flask

# 6. Get the app server to be able to serve static pages by adding the following lines,
# below the import flask line.
# The static folder points to the directory that contains the html pages.
app = Flask(__name__,
             static_url_path='', 
             static_folder='../')
            
@app.route('/')
def index():
    return"Hello, World!"
# 5. In your terminal c+p 127.0.0.1:5000 into your browser,
# Should output Hello World.

if __name__ == '__main__' :
    app.run(debug= True)