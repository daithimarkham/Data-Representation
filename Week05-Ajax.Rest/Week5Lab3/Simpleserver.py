#!flask/bin/python
from flask import Flask

# 6. Get the app server to be able to serve static pages by adding the following lines,
# below the import flask line.
# The static folder points to the directory that contains the html pages.

app = Flask(__name__,
             static_url_path='', 
             static_folder='../') # tells Flask where to find static content.
            
@app.route('/') # after hostname in url, call function if forward slash.
def index():
    return"Hello, World!" # function outputs hello world as a http response.
# 5. In your terminal c+p 127.0.0.1:5000 into your browser,
# Should output Hello World.

if __name__ == '__main__' : # if name is main, run Flask
    app.run(debug= True)