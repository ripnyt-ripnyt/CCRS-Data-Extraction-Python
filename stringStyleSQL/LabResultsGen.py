import csv
import re

# ------------------------------------------ #
#                      Config                 #
# ------------------------------------------ #
filename = 'G:\CleanCCRS\compccrs\LabResult_0.csv'

tableName = 'lab_results'
fileMap = {
    'lab_result_id'     : "int", 
    'lab_licensee_id'   : "int", 
    'licensee_id'       : "int", 
    'lab_test_status'   : "varchar",
    'inventory_item_id' : "int", 
    'test_name'         : "varchar",
    'test_date'         : "datetime", 
    'test_value'        : "varchar",
    'external_id'       : "varchar", 
    'status'            : "varchar",
    'created_by'        : "varchar",
    'created_date'      : "datetime",
    'updated_by'        : "varchar",
    'updated_date'      : "datetime"
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
        outputFile = open("G:\CleanCCRS\compccrs\LabResults_0.sql", "a",  encoding='utf-8')
        outputFile.writelines(outputSql)
        outputFile.close()
        
        print(outputSql)
        valuesString = ""