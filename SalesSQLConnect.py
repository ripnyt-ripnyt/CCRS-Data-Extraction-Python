import csv
import os
import mysql.connector
from mysql.connector import Error

# ------------------------------------------ #
#                      Config                 #
# ------------------------------------------ #
directory = 'C:/Users/ripny/Desktop/compccrs/cleanup/src/'


tableName = 'sales'
fileMap = {
    'sale_id' : "varchar",
    'seller_licensee_id' : "varchar",
    'purchaser_licensee_id' : "varchar",
    'sale_type' : "varchar",
    'sale_date' :"datetime",
    'external_id' : "varchar",
    'status' : "varchar",
    'created_by' : "varchar",
    'created_date' : "datetime",
    'updated_by' : "varchar",
    'updated_date' : "datetime"
}

    # ------------------------------------------ #
    #         Setup column names in sql string   #
    # ------------------------------------------ #
params = ''
insertString = "INSERT INTO " + tableName + " ("
for key in fileMap:
    insertString += key + ", "
    params += '%s, '

insertString = insertString[:-2] + ') VALUES (' + params[:-2] + ')'
print(insertString)

    # ------------------------------------------ #
    #         loop all files in folder           #
    # ------------------------------------------ #
i = 0

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    values = []
    
    #open database

    database = mysql.connector.connect( host='localhost',
                            database='mason',
                            user='root',
                            password='ZIN8HF43')
    mycursor=database.cursor()
    mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    # ------------------------------------------ #
    #                 Loop CSV  for values       #
    # ------------------------------------------ #
    with open(f, 'rt') as csvFile: 
        print("file being processed: ", f)
        datareader = csv.reader(csvFile)
        next(datareader)
        
        for row in datareader:
            valuesList = []
            for column in row:
                 # Check for null first
                if (len(column) < 1):
                    valuesList.append(None)
                    
                # Integer
                elif (fileMap[key] == "int"):
                    valuesList.append(column)
                                    
                # Varchar
                elif (fileMap[key] == "varchar"):
                    if (key == 'status'):
                        if (column == '\'False\''):
                            valuesList.append("\'Active\')")
                        elif (column == '\'True\''):
                            valuesList.append("\'Deleted\')")
                    else:
                        valuesList.append(column)

                # DateTime
                elif (fileMap[key] == "datetime"):
                    valuesList.append(column)
            values.append(tuple(valuesList))

    try:
        print('Connecting to MySQL database...')

        if database.is_connected():
            print('Connection established.')
            mycursor.executemany(insertString,values)
            database.commit()
        else:
            print('Connection failed.')

    except Error as e:
        print(mycursor.statement)
        print(e)
        

    finally:
        if database is not None and database.is_connected():
            database.close()
            mycursor.close()
            print('Connection closed.')
        
    print(mycursor.rowcount, "was inserted.")