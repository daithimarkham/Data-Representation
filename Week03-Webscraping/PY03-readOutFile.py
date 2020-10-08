# David Markham
# 08/10/2020
# Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol,
# or through a web browser.

# Here we look for the first “tr” element in our file and print it out.

from bs4 import BeautifulSoup # Makes page look more attractive.

with open("../Week02-Java/Lab2CarViewer.html") as fp: # fp = file pointer
    soup = BeautifulSoup(fp, 'html.parser')

# print (soup.tr) # This prints first element that has the tr tag in the file.



rows = soup.findAll("tr") # tr defines a row in html. This will print out all tr tags.
for row in rows:
    #print("........") # ..... put a line between each tr tag
    #print(row) # gets all the tr tags in each row
    
    datalist = [] # search for the td tags(table data) and modifies the data so stored in a list
    cols = row.findAll("td") # Setting variable to find all the td tags.
    for col in cols:
        datalist.append(col.text) # Append datalist
    print (datalist) # Prints datalist 