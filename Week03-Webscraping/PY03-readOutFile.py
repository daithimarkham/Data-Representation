# David Markham
# 10/10/2019 
# Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol,
# or through a web browser.


from bs4 import BeautifulSoup

with open("../Week02-Java/Lab2CarViewer.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# print (soup.tr) # first element that has the tr tag



rows = soup.findAll("tr") # tr defines a row in html
for row in rows:
    #print("........") # ..... put a line between each tr tag
    #print(row) # gets all the tr tags in each row
    
    datalist = [] # search for the td tags(table data) and modifies the data so stored in a list
    cols = row.findAll("td")
    for col in cols:
        datalist.append(col.text)
    print (datalist) 