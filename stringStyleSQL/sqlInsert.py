import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='mason',
                                       user='root',
                                       password='ZIN8HF43')
        
        mycursor = conn.cursor()
        if conn.is_connected():
            print('Connected to MySQL database')
        mycursor.execute("INSERT INTO sale_items (`sale_item_id`,`sale_id`,`inventory_item_id`,`licensee_id`,`plant_id`,`quantity`,`price`,`discount`,`sales_tax`,`other_tax`,`status`,`created_by`,`created_date`,`updated_by`,`updated_date`) VALUES (SaleDetailId,SaleHeaderId,InventoryId,PlantId,Quantity,UnitPrice,'CreatedBy','CreatedDate','UpdatedBy','UpdatedDate'")
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()