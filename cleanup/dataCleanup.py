import csv
import os
import re


# config for the complete change from raw to in sql
reqColumns = 8

directorySrc =          'C:/Users/ripny/Desktop/compccrs/cleanup/src/'
directoryASCII =        "C:/Users/ripny/Desktop/compccrs/cleanup/ASCII/"
directoryUTF8 =         "C:/Users/ripny/Desktop/compccrs/cleanup/UTF8/"
directoryMySQLSource =  "C:/Users/ripny/Desktop/compccrs/cleanup/directoryMySQLSource/"
errorFolder =           "C:/Users/ripny/Desktop/compccrs/cleanup/errors/"

# Dialects for reading in .csv files.
class customDialect(csv.Dialect):
    """Describe the usual properties of Excel-generated CSV files."""
    delimiter = '\t'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL
csv.register_dialect("customDialect", customDialect)
#clean out non-ascii characters

'''

for filename in os.listdir(directorySrc):
    f = os.path.join(directorySrc, filename)
    print(f + " is removing non-ascii char")
    with open(f, 'r', encoding="utf-16-le") as source_file:
        datareader = csv.reader(source_file, dialect= 'customDialect')
        with open(os.path.join(directoryASCII,filename), "w", encoding="utf-16-le") as dest_file:
            datawriter = csv.writer(dest_file, dialect= 'customDialect')
            for row in datareader:
                for i, val in enumerate(row):
                    row[i] = ''.join([c if ord(c) < 128 else '' for c in val])
                datawriter.writerow(row)
            print(str(datareader.line_num), ' lines written from raw')
            dest_file.close()
        source_file.close()


#change encoding

for filename in os.listdir(directoryASCII):
    f = os.path.join(directoryASCII, filename)
    print(f + ": is changing encoding")
    with open(f, 'rt', encoding="utf-16-le") as source_file:
        datareader = csv.reader(source_file, dialect= 'customDialect')
        with open(os.path.join(directoryUTF8,filename), "a+b") as dest_file:
            with open(f, 'rb') as source_file:
                contents= source_file.read()
                dest_file.write(contents.decode('utf-16-le').encode('utf-8'))
            print(str(datareader.line_num), ' lines written from ASCII') 
        dest_file.close()
    source_file.close()

'''

# setup a csv with the good formated rows
valuesList = []
values = []


for filename in os.listdir(directoryUTF8):
    f = os.path.join(directoryUTF8, filename)
    o = os.path.join(directoryMySQLSource, filename)
    e = os.path.join(errorFolder, filename)
    print(f + ' is losing columns')
    with open(f, 'rt', encoding='utf-8') as csvFile:
        with open(o, "a", encoding="utf-8") as outputFile:
            datareader = csv.reader(csvFile, dialect='customDialect')
            datawriter = csv.writer(outputFile, dialect='customDialect')
            with open(e, 'a', encoding='utf-8') as errorFile:
                
                for row in datareader:
                    valuesList = []
                    errorOut = ""
                    clean = ''
#building a list of strings
                    for column in row:
                        valuesList.append(column)
#checking for correct # of columns, and troubleshooting
                    if len(valuesList) < reqColumns:
                        print(valuesList)
                    while reqColumns < len(valuesList):
                        valuesList[2] = valuesList[2] + valuesList[3]
                        del valuesList[3]
                    clean = valuesList[2]
                    while clean !=
                        clean = valuesList[2]
                        clean.replace('"','')
                        clean.replace('\\t','')
                        clean.replace('\\','')
                        if clean.isascii() != 1:
                            re.sub('[^\x00-\x7f]', '', clean)
                        if
                        errorOut = str(row) + '\n'
                        errorFile.writelines(errorOut)
                else:
                    datawriter.writerow(valuesList)
            values.append(tuple(valuesList))

            print(str(datareader.line_num), ' lines written from UTF8')
