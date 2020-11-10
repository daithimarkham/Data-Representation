# David Markham 
# 11-10-2020

# In this lab we are going to use Python access APIs that need a key
# We are using the APIs as described by:
# https://developer.github.com/v3/guides/ 

import requests
import json


# remove the minus sign
# this API key no longer works, probably because someone saved it to GitHub
# I have made a new one and posted to  learnonline

# API KEY needs to be commented out if uploading to github, security reasons.
apiKey = '7aa146eafee094d3a7b1e81aa1d8fcb0eec8b910' 
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey)) # token is username, api key is password.

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4) 

# This API key was incorrect. You can see by the repo.json file, f you click in, no info 
# has been retrieved, just bad credentials. 