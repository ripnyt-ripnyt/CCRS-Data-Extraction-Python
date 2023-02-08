import csv
import os
import codecs
import shutil
import zipfile

# config for the complete change from raw to in sql
reqColumns = 8

src =  "/mnt/GIS/CCRS_DATA/"
utf8 = "/mnt/GIS/CCRS_DATA/INFLATED_FILES/"
ascii_folder = "/mnt/GIS/CCRS_DATA/ASCII_CHAR_ONLY"

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

write_count = 0
for root, dirs, files in os.walk(src):
    for file in files:
        if file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                zip_ref.extractall(utf8)
                extracted_file = zip_ref.namelist()[0]
                extracted_file_base = os.path.basename(extracted_file)
                extracted_file_path = os.path.join(utf8, extracted_file)
                with codecs.open(extracted_file_path, encoding='utf-16-le', errors='replace') as source_file:
                    dest_file_base = extracted_file_base.rsplit('\\', 1)[-1]
                    dest_file_base = dest_file_base[:-4] + ".tsv"
                    dest_file_path = os.path.join(ascii_folder, dest_file_base)
                    if os.path.exists(dest_file_path):
                        print("File already exists in the ASCII_CHAR_ONLY directory, skipping processing.")
                        continue
                    with codecs.open(dest_file_path, 'w', encoding='utf-8') as dest_file:
                        for row in source_file:
                            row = ''.join(
                                [c if ord(c) < 128 else '' for c in row])
                            dest_file.write(row)
                        write_count += 1
            os.remove(extracted_file_path)
print('files written: ' + str(write_count))


## TABLE TYPE SPECIFIC

#for filename in os.listdir(ascii):
#    f = os.path.join(ascii, filename)
#    o = os.path.join(dest, filename)
#    e = os.path.join(error, filename)
#    print(f + ' is losing columns')
#    with open(f, 'rt', encoding='utf-8') as csvFile:
#        with open(o, "a", encoding="utf-8") as outputFile:
#            datareader = csv.reader(csvFile, dialect='customDialect', )
#            datawriter = csv.writer(outputFile, dialect='customDialect')
#            with open(e, 'a', encoding='utf-8') as errorFile:
#                for row in datareader:
#                    valuesList = []
#                    errorOut = ""
#                    for column in row:
#                        valuesList.append(column)                           #building a list of strings
#                    if len(valuesList) < reqColumns:                        #checking for correct # of columns, and troubleshooting
#                        print(valuesList)
#                    while reqColumns < len(valuesList):
#                        valuesList[2] = valuesList[2] + valuesList[3]       #this uses the observation that the names column in strains table has tabs in it
#                        del valuesList[3]                                   #will need to be modified for other tables?
#                    datawriter.writerow(valuesList)
#            values.append(tuple(valuesList))
#            print(str(datareader.line_num), ' lines ready for SQL-Python-Connect')
#    os.remove(f)
