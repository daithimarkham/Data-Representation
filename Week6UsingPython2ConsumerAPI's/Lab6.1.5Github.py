# David Markham
# 11-10-2020

# Challenge read from github
# Create a spread sheet that gets all the users that are following me ,
# and outputs the users login and repos URL to a spreadsheet.

# A. Get the list from the the github API and output to the console (messy)
# B. Then output it to a file neatly
# C. Now you have to work out how you would write this to excel

import requests, json 

def getJSONFromUrl(url):
    response = requests.get(url)
    data = response.json()
    return data

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

data = getJSONFromUrl(url)
# Print (data)
# Get the file name for the new file to write

filename = 'githubusers.json'

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4) 
