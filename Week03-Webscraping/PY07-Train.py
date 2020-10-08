# David Markham 
# 08/10/2020
# This program gets all the trains that are located south of Dublin,
# and stores the data associated with them. 
# A program like this would normally store all the data into the csv file, 
# and let another part of the program analysis the data.
# I am only doing this to demonstrate how you can reduce a dataset as you are reading it
# (you would want to do it with exceptionally large datasets, not like this one).


# Import all libraries
# Part 1&2. Get the data. Create a python program that reads the XML from the URL and prints it out,
# using beautifulSoup. Check it does retrieve the data.
import requests
import csv
from bs4 import BeautifulSoup
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML" # # URL we will import.
page = requests.get(url) # Retrieves data from webpage.

soup = BeautifulSoup(page.content, 'xml') # Makes data appear more user friendly.  
#print (soup.prettify()) Part 1&2 & 3 done.

# Part 8. (A) Make ARRAY called retrieveTags, will store all names of tags we want to retrieve.
retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

# Part 6. A Let’s now store this one property into a CSV:
# Before the for loop open the CSV file, I am using with, so make sure that,
# you indent the for loop so that it is in the with block.
with  open('week03_train.csv', mode='w') as train_file: #  enabling write mode, open csv, with write mode as train file.
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL) # How to create delimiter, char and quoting.

# Part 4 and 5. Modify the program to print out each of the trains. I.e. find the listings and
# iterate through them to print each out. Check it works
    listings = soup.findAll("objTrainPositions") # Find all the train listings. 

    for listing in listings: # Iterate through listings
        #print(listing)
        print(listing.TrainLatitude.string) # Print out all the listings.
        # or 
        # Comment out the print and modify the program so that it prints out the latitudes
        # print(listing.find('TrainLatitude').string) Part 4 and 5 done.

# Part 9. We are only going to store trains that are south of Dublin, IE have a latitude less
# then that of Dublin (approx. 53.4)
        lat =float( listing.TrainLatitude.string) # stores train latitude less that of:
        if (lat < 53.4): # 53.4 which is Dublin, will output all trains less than that, are south of Dublin.
# Part 6. B: In the for loop now create an array called entryList
# append in the latitude and store that in the CSV.
            entryList = [] # Create array called entrylist
            for retrieveTag in retrieveTags:
                entryList.append(listing.find(retrieveTag).string) # append latitude 
            train_writer.writerow(entryList) # and store in CSV
# Part 7. Run program and see if csv file saved the stores of latitude.
            


