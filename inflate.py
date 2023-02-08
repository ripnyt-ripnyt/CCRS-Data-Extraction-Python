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

#############################################

# From Chat GPT

#############################################

def extract_zip(zip_path, dest_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            # Extract the file to the destination directory
            zip_ref.extract(file, dest_dir)
            # Get the absolute file path
            file_path = os.path.join(dest_dir, file)
            # Split the file path into the directory and filename
            dirname, filename = os.path.split(file_path)
            # Write the file to the destination directory without preserving the hierarchy
            shutil.move(file_path, os.path.join(dest_dir, filename))
