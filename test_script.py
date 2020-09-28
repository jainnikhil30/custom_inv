import os
import glob
import csv

from xlsxwriter.workbook import Workbook
workbook = Workbook('/var/lib/awx/config-test/vCMP-config-report.xlsx')
print("Hello, World!")
for csvfile in glob.glob(os.path.join('', '*.csv')):
    print("Hello, World! - 2")
    worksheet = workbook.add_worksheet(os.path.splitext(csvfile)[0]) # worksheet with csv file name
    print("Hello, World! - 4")
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        print("Hello, World! - 4")
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col) # write the csv file content into it
workbook.close()
