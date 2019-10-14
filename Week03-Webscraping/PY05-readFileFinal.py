# David Markham 11/10/2019
# Bringing code together from previous files.

from bs4 import BeautifulSoup
import csv

with open("../Week02-Java/Lab2CarViewer.html") as fp:
    soup = BeautifulSoup(fp, "html.parser") 

employee_file = open('Week03-Java.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
for row in rows:

    cols = row.findAll("td")
    datalist = [] 
    for col in cols:
        datalist.append(col.text)
    employee_writer.writerow(datalist)
employee_file.close()

# Need to add code which hides update and delete.

    