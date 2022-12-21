import pandas as pd
import zipfile
import os

os.remove

# Input
data_file = "Strains_0.zip"

# The max column count a line in the file could have
largest_column_count = 12

### Loop the data lines
with open(data_file, 'r', encoding= 'latin_1') as temp_f:
    # get No of columns in each line
    col_count = [ len(l.split("\t")) for l in temp_f.readlines() ]

### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
column_names = [i for i in range(0, max(col_count))]
column_names_str = list(map(str, column_names))

### Read csv
df = pd.read_csv(data_file, header=None, delimiter='\t', index_col=0, encoding= 'latin_1')
df.head