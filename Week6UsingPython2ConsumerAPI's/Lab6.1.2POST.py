# David Markham
# Write a python program that creates a car on the server by using the API.


# Import packages
import requests
import json

# Create car and add to page.
dataString = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','price':12324} 
url = 'http://127.0.0.1:5000/cars' # add to URL

response = requests.post(url, json=dataString) # Post request to url, using json 

print (response.status_code) # Prints status code to terminal.