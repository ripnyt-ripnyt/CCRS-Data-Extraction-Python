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

tableName = 'areas'
fileMap = {
    'area_id'       : 'int',  
    'licensee_id'   : 'int', 
    'name'          : 'varchar', 
    'is_quarantine' : 'varchar', 
    'external_id'   : 'varchar', 
    'status'        : 'varchar', 
    'created_by'    : 'varchar', 
    'created_date'  : 'datetime', 
    'updated_by'    : 'varchar', 
    'updated_date'  : 'datetime'
}

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