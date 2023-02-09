import csv
import re

# ------------------------------------------ #
#                      Config                 #
# ------------------------------------------ #
filename = 'G:\CleanCCRS\compccrs\Inventory_0.csv'

tableName = 'inventory_items'
fileMap = {
    "inventory_item_id": "varchar",
    "licensee_id": "varchar",
    "strain_id": "varchar",
    "area_id": "varchar",
    "product_id": "varchar",
    "inventory_identifier": "varchar",
    "initial_quantity": "varchar",
    "quantity_on_hand": "varchar",
    "total_cost": "varchar",
    "is_medical": "varchar",
    "external_id": "varchar",
    'status': "varchar",
    'created_by': "varchar",
    'created_date': "datetime",
    'updated_by': "varchar",
    'updated_date': "datetime"
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
        outputFile = open("G:\CleanCCRS\compccrs\InventoryItems_0.sql", "a",  encoding='utf-16-le')
        outputFile.writelines(outputSql)
        outputFile.close()
        
        print(outputSql)
        valuesString = ""