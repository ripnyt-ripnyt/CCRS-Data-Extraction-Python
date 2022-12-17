import csv
import os
import mysql.connector
from mysql.connector import errors

# ------------------------------------------ #
#                      Config                 #
# ------------------------------------------ #
directory = 'C:/Users/ripny/Desktop/compccrs/sales'

database = mysql.connector.connect( host='localhost',
                            database='mason',
                            user='root',
                            password='ZIN8HF43')

conn = None

mycursor=database.cursor()

try:
    print('Connecting to MySQL database...')
    

    if database.is_connected():
        print('Connection established.')
        serverStatus = mycursor.execute('SHOW ENGINE INNODB STATUS')
        print(serverStatus[0])
        database.commit()
    else:
        print('Connection failed.')

except mysql.connector.IntegrityError as err:
    print(err)

finally:
    if database is not None and database.is_connected():
        database.close()
        print('Connection closed.')