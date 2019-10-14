# David Markham
# 10/10/2019 

import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page) # The header
print("-------------------") 
print (page.content) # The content
soup1 = BeautifulSoup(page.content, 'html.parser')
print (soup1.prettify()) # Makes it more beautiful with the parser