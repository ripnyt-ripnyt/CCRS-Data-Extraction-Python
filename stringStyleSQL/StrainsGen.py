import csv
import re
import os

# ------------------------------------------ #
#                      Config                 #
# ------------------------------------------ #
directory = 'C:/Users/ripny/Desktop/compccrs/src'
output_directory = "C:/Users/ripny/Desktop/compccrs/dest"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    tableName = 'strains'
    fileMap = {
        'strain_id' : 'int',
        'strain_type' : 'varchar', 
        'name' : 'varchar', 
        'status' : 'varchar', 
        'created_by' : 'varchar', 
        'created_date' : 'datetime', 
        'updated_by' : 'varchar', 
        'updated_date' : 'datetime',
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
    with open(f, 'rt') as csvFile:
        datareader = csv.reader(csvFile, UnicodeEncodeError)
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
            print(valuesString)
            sizeFileName=len(filename)
            modFileName= filename[:sizeFileName - 4]
            outputSql = insertString[:-1] + ") " + valuesString[:-1] + ");\n"        
            outputFile = open(os.path.join(output_directory, modFileName +".sql"), "a")
            outputFile.writelines(outputSql)
            outputFile.close()
            
            
            valuesString = ""