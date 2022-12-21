import zipfile
import shutil
import os

folder = os.getcwd()

# Open the zip file

#get list of files
zip_file_list = [f for f in os.listdir(folder) if f.endswith(".zip")]


# Extract the csv file from the zip file

for zip_file in os.listdir(folder)
csv_name = zip_file.namelist()[0]
csv_file = zip_file.open(csv_name)

# Create a new tsv file
tsv_name = csv_name[:-3] + 'tsv'
tsv_file = open(tsv_name, 'w')

# Copy the contents of the csv file to the tsv file
shutil.copyfileobj(csv_file, tsv_file)

# Close the files
csv_file.close()
tsv_file.close()
zip_file.close()

# Remove the zip file
os.remove(zip_name)
