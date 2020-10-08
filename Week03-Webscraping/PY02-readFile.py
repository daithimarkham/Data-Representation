# David Markham
# 14/10/2019
# Read from previous weeks html - Carviewer 

from bs4 import BeautifulSoup # makes page more attractive and user friendly.

# Parsers are programs that read the text and convert that into DOM trees.
with open("../Week02-Java/Lab2CarViewer.html") as fp: # opens file from directory.
    soup = BeautifulSoup(fp,"html.parser") # fp = file pointer

print (soup.prettify()) # Prints file and makes page more attractive for user.

