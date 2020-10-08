# David Markham 11/10/2019
# Webcraping - CSV File
# Write to a CSV file using the CSV package.

import csv # Library to import csv files.

employee_file = open('employee_file.csv', mode='w') # what file to open. mode=w = write. Creates file in this directory.
# Now we make a variable called employee_writer. Delimiter we use, quoate char will look like, and minimal amount of quiting is necessary.
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 

# Here we create two new rows.
employee_writer.writerow(['John Malone', 'Accounting', 'November']) # Write row
employee_writer.writerow(['Erica Meyers', 'IT', 'March']) # Write row.

employee_file.close() # Then close file when finished with it. 