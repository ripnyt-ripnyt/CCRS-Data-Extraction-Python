import csv
import re
import os
#import mysql.connector

# ------------------------------------------ #
#                      Config                 #
# ------------------------------------------ #
directory = 'C:/Users/ripny/Desktop/compccrs/src'
#database = mysql.connector.connect(host='localhost',
#                                    database='mason',
#                                    user='root',
#                                    password='ZIN8HF43')

# output_directory = "C:/Users/ripny/Desktop/compccrs/salesdetailsql"

tableName = 'sale_items'
fileMap = {
    'sale_item_id': "int",
    'sale_id' : "int",
    'inventory_item_id' : "int", 
    'plant_id' : "int",
    'quantity' : "int", 
    'price'     : "int", 
    'discount'  : "int",
    'sales_tax' : "int",
    'other_tax' : "int",
    'external_id' : "varchar",
    'status' : "varchar",
    'created_by'   : "varchar",
    'created_date' : "datetime",
    'updated_by'   : "varchar",
    'updated_date' : "datetime"
}

    # ------------------------------------------ #
    #         Setup column names in sql string   #
    # ------------------------------------------ #
params = ''
insertString = "INSERT INTO " + tableName + " ("
for key in fileMap:
    insertString += " " + key + ","
    params += '%s, '

insertString = '\"' + insertString[:-1] + ') VALUES (' + params[:-2] + ')\"'

    
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    
    # ------------------------------------------ #
    #                 Loop CSV  for values       #
    # ------------------------------------------ #
    with open(f, 'rt') as csvFile:
        datareader = csv.reader(csvFile)
        for row in datareader:
            valuesString = ""
            csvIndex = 0
            for key in fileMap:

                # Check for null first
                if (len(row[csvIndex]) < 1):
                    valuesString += '\"NULL\",' 

                # Integer
                elif (fileMap[key] == "int"):
                    valuesString += '\"' + re.sub(' +', ' ',row[csvIndex]).rstrip() + "\","
                    
                # Varchar
                elif (fileMap[key] == "varchar"):
                    if (key == 'status'):
                        if (row[csvIndex] == '\"False\"'):
                            valuesString += "\"Active\","
                        elif (row[csvIndex] == '\"True\"'):
                            valuesString += "\"Deleted\","
                    else:
                        valuesString += "\"" + re.sub(' +', ' ',row[csvIndex]).rstrip() + "\","

                # DateTime
                elif (fileMap[key] == "datetime"):
                    valuesString += "\"" + re.sub(' +', ' ',row[csvIndex]).rstrip() + "\","
                csvIndex += 1

            valuesString = "(" + valuesString[:-1] + ")"
            print(valuesString)
            
    # ------------------------------------------ #
    #          insert into table w/connector     #
    # ------------------------------------------ #


    # ------------------------------------------ #
    #                Save to output file         #
    # ------------------------------------------ #
            #sizeFileName=len(filename)
            #modFileName= filename[:sizeFileName - 4]
            #outputFile = open(os.path.join(output_directory, modFileName +".sql"), "a")
            #outputFile.writelines(outputSql)
            #outputFile.close()
            
            #print(outputSql)
            valuesString = ""