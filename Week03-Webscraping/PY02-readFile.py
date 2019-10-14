# David Markham
# 14/10/2019
# Read from previous weeks html - Carviewer 

from bs4 import BeautifulSoup

with open("../Week02-Java/Lab2CarViewer.html") as fp:
    soup = BeautifulSoup(fp,"html.parser") # fp = file pointer

print (soup.prettify())

