import mysql.connector
from mysql.connector import Error

database = mysql.connector.connect( host='localhost',
                            database='mason',
                            user='root',
                            password='ZIN8HF43')

mycursor=database.cursor()

conn = None

try:
    print('Connecting to MySQL database...')

    if database.is_connected():
        print('Connection established.')
        print(mycursor.statement)
        #mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        results = mycursor.fetchone()
        print(results)
    else:
        print('Connection failed.')

except Error as e:
    print(mycursor.statement)
    print(e)
    

finally:
    if database is not None and database.is_connected():
        database.close()
        print('Connection closed.')
    