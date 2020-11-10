import requests
import json
from xlwt import * # Built in package for excel files

# Sending https response requests
# Can use it to retrieve certain info
# print(response.headers) will get all headers on page
# print(response.status.code) get code back 200, etc. 
# print(response.text) gets all data and text from pages. 
url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

# Output to console
print (data)

# Output cars individually 
for car in data["cars"]:
    print (car)

# Other code
# Save this to a file
filename = 'cars.json'
if filename:
    # Writing JSON data
    with open(filename, 'w') as f: # open file for writing, creates one if it does not exist.
        json.dump(data, f, indent=4) # get rid of previous data using dump. 
        # Indent displays data more clearly when using large files.

# Write to excel file
w = Workbook()
ws = w.add_sheet('cars')
row = 0;
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1 
for car in data["cars"]:
    ws.write(row,0, car["reg"])
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row += 1

w.save('cars.xls') 