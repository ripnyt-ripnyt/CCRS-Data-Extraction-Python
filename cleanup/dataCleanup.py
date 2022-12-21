import csv
import os
import codecs
import shutil
import zipfile

# config for the complete change from raw to in sql
reqColumns = 8

src =     "C:/Users/DevinErgler/Documents/GitHub/CCRS-Python-MySQL/cleanup/src/"
ascii =   "C:/Users/DevinErgler/Documents/GitHub/CCRS-Python-MySQL/cleanup/ascii/"
utf8 =   "C:/Users/DevinErgler/Documents/GitHub/CCRS-Python-MySQL/cleanup/utf8/"
dest =    "C:/Users/DevinErgler/Documents/GitHub/CCRS-Python-MySQL/cleanup/dest/"
error =   "C:/Users/DevinErgler/Documents/GitHub/CCRS-Python-MySQL/cleanup/error/"

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

# walk through all sub directories in a .zip, read the src as a utf-16-le and output a utf-8 file.
# DO NOT run on all .zips, they must be of the same table type, since the concat function later isn't ready.
# consider leaving that to custom cleanup scripts and splitting this script out, as an 'inflation'.

for root, dirs, files in os.walk(src):
    for file in files:
        if file.endswith(".zip"):
            # Open the zip file and extract the first file from it
            with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                # Extract the first file from the zip archive
                zip_ref.extractall(utf8)
                extracted_file = zip_ref.namelist()[0]
                extracted_file_path = os.path.join(utf8, extracted_file)
                dirname, file = os.path.split(extracted_file_path)
                dirname, _ = os.path.split(dirname)
            # Open the extracted file and re-encode it as utf-8
            with codecs.open(extracted_file_path, encoding='utf-16-le') as source_file:
                # Create a new file with the same name but with .tsv extension
                dest_file_path = os.path.join(dirname, file[:-4] + ".tsv")
                
                with codecs.open(dest_file_path, 'w', encoding='utf-8') as dest_file:
                    # Copy the contents of the source file to the destination file
                    shutil.copyfileobj(source_file, dest_file)
            # Remove the extracted file
            os.remove(extracted_file_path)
#clean out non-ascii characters, punctuation

for filename in os.listdir(utf8):
    f = os.path.join(utf8, filename)
    print(f + " is removing non-ascii char")
    with open(f, 'r', encoding="utf-8") as source_file:
        datareader = csv.reader(source_file, dialect= 'customDialect')
        with open(os.path.join(ascii,filename), "w", encoding="utf-8") as dest_file:
            datawriter = csv.writer(dest_file, dialect= 'customDialect')
            for row in datareader:
                for i, val in enumerate(row):
                    row[i] = ''.join([c if ord(c) < 128 else '' for c in val])
                datawriter.writerow(row)
            dest_file.close()
        source_file.close()
    os.remove(f)
# Eliminate the extra tabs
valuesList = []
values = []


## TABLE TYPE SPECIFIC

for filename in os.listdir(ascii):
    f = os.path.join(ascii, filename)
    o = os.path.join(dest, filename)
    e = os.path.join(error, filename)
    print(f + ' is losing columns')
    with open(f, 'rt', encoding='utf-8') as csvFile:
        with open(o, "a", encoding="utf-8") as outputFile:
            datareader = csv.reader(csvFile, dialect='customDialect', )
            datawriter = csv.writer(outputFile, dialect='customDialect')
            with open(e, 'a', encoding='utf-8') as errorFile:
                for row in datareader:
                    valuesList = []
                    errorOut = ""
                    for column in row:
                        valuesList.append(column)                           #building a list of strings
                    if len(valuesList) < reqColumns:                        #checking for correct # of columns, and troubleshooting
                        print(valuesList)
                    while reqColumns < len(valuesList):
                        valuesList[2] = valuesList[2] + valuesList[3]       #this uses the observation that the names column in strains table has tabs in it
                        del valuesList[3]                                   #will need to be modified for other tables?
                    datawriter.writerow(valuesList)
            values.append(tuple(valuesList))
            print(str(datareader.line_num), ' lines ready for SQL-Python-Connect')
    os.remove(f)
