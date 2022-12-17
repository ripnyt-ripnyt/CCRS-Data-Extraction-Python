import os
import csv

#clean out non-ascii characters

directorySrc =          'C:/Users/ripny/Desktop/compccrs/cleanup/src/'
directoryASCII =        "C:/Users/ripny/Desktop/compccrs/cleanup/ASCII/"
enc = "utf-8"

for filename in os.listdir(directorySrc):
    f = os.path.join(directorySrc, filename)
    print(f + " is removing non-ascii char")
    with open(f, 'r', encoding="enc") as source_file:
        datareader = csv.reader(source_file, quotechar=None)
        with open(os.path.join(directoryASCII,filename), "w", encoding="utf-16-le") as dest_file:
            for row in datareader:
                for i, val in enumerate(row):
                    row[i] = ''.join([c if ord(c) < 128 else '' for c in val])
                dest_file.writelines(row)
                dest_file.writelines('\n')
            dest_file.close()