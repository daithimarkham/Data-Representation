# David Markham
# 14/10/2019
# Below we will extract data from a URL address.
# How to find data, elements, classes etc from a webpage,
# So you can navigate to data which you want in an easy manner.

import requests
import csv
from bs4 import BeautifulSoup
url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"
page = requests.get(url) 

soup = BeautifulSoup(page.content, "html.parser") 

home_file = open("Week03MyHome.csv", mode="w")
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Find the Div where the class equals the property listing card.
listings = soup.findAll("div", class_="PropertyListingCard" )

# Creates a list which will be saved into CSV
for listing in listings:
    entryList = []
#Find the price under listings and fetch the text out of that.s
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
# Get the address the same way.
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)
# Writes it into the CSV file.s
    home_writer.writerow(entryList) 
home_file.close() # Close the file