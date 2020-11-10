# David Markham 
# 11-10-2020

# In this lab we are going to use Python access APIs that need a key
# We are using the APIs as described by:
# https://html2pdf.app/ 
# Create a PDF file from a url page.

import requests
import json
# 1. Write a python program that will read in a html page from a file and prints it out again.
#html = '<h1>hello world</h1>This is html'
f = open("../week02-Java/Lab2CarViewer.html", "r") # opens in carviewer from week2
html = f.read() # read it in
#print (html)

# 2. Modify the script to use the html2pdf.app api with the key: 
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate' # Script prints out status of the code.

data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data) # post request
print (response.status_code) # gives response to confirm it works

# Modify the program to write the binary data returned to a file .pdf
newFile = open("Lab6.2.1.htmlaspdf.pdf", "wb") # open up new file, pdf.
newFile.write(response.content) # take content and print it out.