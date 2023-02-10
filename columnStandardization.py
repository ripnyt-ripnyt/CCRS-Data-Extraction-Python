import csv
import os
import pandas as pd

# running this removed old files to save disk space, comment out the os.remove() line to retain them.
src = '/src/path/with/inflated/csvs'
dest = '/dest/path/for/standardized/column/width/csvs'

df_results = pd.DataFrame(columns=['file', 'columns_removed'])
df_bad_rows = pd.DataFrame(columns=['file', 'row', 'element', 'next_element'])


# Dialects for reading in .csv files.
class customDialect(csv.Dialect):
    """Describe the usual properties of Excel-generated CSV files."""
    delimiter = '\t'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL


csv.register_dialect("customDialect", customDialect)

# 'file prefix' : (length of row list, location of field which has delimiters)

file_types = {
    'Areas_': (10, 2),
    'Contacts_': (13, 0),
    'Integrator_': (7, 1),
    'Inventory_': (16, 1),
    'InventoryAdjustment_': (12, 3),
    'InventoryPlantTransfer_': (17, 0),
    'LabResult_': (14, 6),
    'Plant_': (18, 0),
    'PlantDestructions_': (11, 7),
    'Product_': (12, 3),  # probably 4 as well, description. 3 is name
    'SaleHeader_': (11, 5),
    'SalesDetail_': (15, 9),
    'Strains_': (8, 2),
    'Licensee_': (22, 4),  #maybe 5 as well, DBA
}

# since the product and licensee issue cells are adjacent, I can likely do nothing and they would be combined fine.

for filename in os.listdir(src):
    reqColumns = 0
    badLocation = 0
    columns_removed = 0
    for key in file_types:
        if filename.startswith(key):
            reqColumns = file_types[key][0]
            badLocation = file_types[key][1]
    f = os.path.join(src, filename)
    filename_csv = filename[:-4] + ".csv"
    o = os.path.join(dest, filename_csv)
    print(f + ' is losing columns')
    with open(f, 'rt', encoding='utf-8') as csvFile:
        columns_removed = 0
        with open(
                o,
                "a",
                encoding="utf-8",
        ) as outputFile:
            datareader = csv.reader(csvFile, dialect='customDialect')
            datawriter = csv.writer(outputFile)
            for row in datareader:
                valuesList = []
                for column in row:
                    valuesList.append(column)
                if len(valuesList) < reqColumns:
                    print(valuesList)
                while reqColumns < len(valuesList):
                    df_bad_row = pd.DataFrame(
                        [[
                            os.path.basename(f), row, valuesList[badLocation],
                            valuesList[badLocation + 1]
                        ]],
                        columns=['file', 'row', 'element', 'next_element'])
                    valuesList[badLocation] = valuesList[
                        badLocation] + valuesList[badLocation + 1]
                    df_bad_rows = pd.concat([df_bad_rows, df_bad_row])
                    del valuesList[badLocation + 1]
                    columns_removed += 1
                datawriter.writerow(valuesList)
        df_result = pd.DataFrame(
            [[os.path.basename(f), str(columns_removed)]],
            columns=['file', 'columns_removed'])
        df_results = pd.concat([df_results, df_result])
    print(o + ' lost ' + str(columns_removed) + ' columns')
    os.remove(f)

df_results.to_csv('df_results.csv', index=False)
df_bad_rows.to_csv('df_bad_rows.csv', index=False)
