import csv
import re

# ------------------------------------------ #
#                      Config                 #
# ------------------------------------------ #
filename = 'G:\CleanCCRS\compccrs\Licensee_0.csv'

tableName = 'licensees'
fileMap = {

    'license_status' : "varchar",
    'licensee_id' : "int",
    'UBI' : "varchar",
    'license_number' : "int",
    'name' : "varchar",
    'dba' : "varchar",
    'license_issue_date' : "datetime",
    'license_expiration_date' : "datetime",
    'external_id' : "varchar",
    'status' : "varchar",
    'address_1' : "varchar",
    'address_2' : "varchar",
    'city' : "varchar",
    'state' : "varchar",
    'zip' : "varchar",
    'county' : "varchar",
    'email' : "varchar",
    'phone' : "varchar",
    'created_by' : "varchar",
    'created_date' : "datetime",
    'updated_by' : "varchar",
    'updated_date' : "datetime"
}

# ------------------------------------------ #
#             Setup column names             #
# ------------------------------------------ #
insertString = "INSERT INTO " + tableName + " ("
for key in fileMap:
    insertString += "`" + key + "`,"

# ------------------------------------------ #
#                 Loop CSV                   #
# ------------------------------------------ #
with open(filename, 'rt', encoding='utf-16-le') as csvFile:
    datareader = csv.reader(csvFile)
    for row in datareader:
        valuesString = "VALUES ("
        csvIndex = 0
        for key in fileMap:

            # Check for null first
            if (len(row[csvIndex]) < 1):
                valuesString += 'NULL,' 

            # Integer
            elif (fileMap[key] == "int"):
                valuesString += re.sub(' +', ' ',row[csvIndex]).rstrip() + ","
                
            # Varchar
            elif (fileMap[key] == "varchar"):
                if (key == 'status'):
                    if (row[csvIndex] == 'False'):
                        valuesString += "'Active',"
                    elif (row[csvIndex] == 'True'):
                        valuesString += "'Deleted',"
                else:
                    valuesString += "'" + re.sub(' +', ' ',row[csvIndex]).rstrip() + "',"

            # DateTime
            elif (fileMap[key] == "datetime"):
                valuesString += "'" + re.sub(' +', ' ',row[csvIndex]).rstrip() + "',"

            csvIndex += 1

        # Save to output file
        outputSql = insertString[:-1] + ") " + valuesString[:-1] + ");\n"        
        outputFile = open("G:\CleanCCRS\compccrs\insertLicenseeSql.sql", "a",  encoding='utf-16-le')
        outputFile.writelines(outputSql)
        outputFile.close()
        
        print(outputSql)
        valuesString = ""