# David Markham
# 10/10/2019 

import requests # import library
from bs4 import BeautifulSoup # Imports beautiful soup to make page easier to read.
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page) # The header
print("-------------------") 
print (page.content) # The content
soup1 = BeautifulSoup(page.content, 'html.parser')
print (soup1.prettify()) # Makes the page more user friendly to read, adjusts layout.