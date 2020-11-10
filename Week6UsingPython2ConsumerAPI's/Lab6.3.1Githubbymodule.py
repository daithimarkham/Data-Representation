# David Markham 
# 11-10-2020

# In this lab we are going to use the package PyGitHub to interact with GitHub,
# It is easier than making all our own requests,

#pip install PyGithub

# 1. install pyGithub
# to use this install package
# pip install PyGithub
from github import Github
import requests 

# remove the minus sign from the key
# you can add this to your code just don't commit it
# or use an API key to your own repo
g = Github("71b89bdc0378f2330931041ef2f2fc573043336-5")

# for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
repo = g.get_repo("datarepresentationstudent/aPrivateOne") # repository from Github
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt") # get file info test.txt
urlOfFile = fileInfo.download_url 
#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text # contents of file 
#print (contentOfFile)
newContents = contentOfFile + " more stuff \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha) # update file, with path.
print (gitHubResponse) 