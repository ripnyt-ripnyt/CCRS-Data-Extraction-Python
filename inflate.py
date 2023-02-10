import csv
import os
import codecs
import zipfile

src = "/src/folder/with/CCRS/Box/Dowload"
temp = "/temp/folder/for/intermediate/file/storage"
dest = "/dest/folder/for/all/inflated/files"


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

# walk through all sub directories in a CCRS  Box Download .zip, read the src as a utf-16-le and output a utf-8 file.
# temp os a temporary location

write_count = 0
for root, dirs, files in os.walk(src):
    for file in files:
        if file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                zip_ref.extractall(temp)
                extracted_file = zip_ref.namelist()[0]
                extracted_file_base = os.path.basename(extracted_file)
                extracted_file_path = os.path.join(temp, extracted_file)
                with codecs.open(extracted_file_path,
                                 encoding='utf-16-le',
                                 errors='replace') as source_file:
                    dest_file_base = extracted_file_base.rsplit('\\', 1)[-1]
                    dest_file_base = dest_file_base[:-4] + ".tsv"
                    dest_file_path = os.path.join(dest, dest_file_base)
                    with codecs.open(dest_file_path, 'w',
                                     encoding='utf-8') as dest_file:
                        for row in source_file:
                            row = ''.join(
                                [c if ord(c) < 128 else '' for c in row])
                            dest_file.write(row)
                        write_count += 1
            os.remove(extracted_file_path)
print('files written: ' + str(write_count))
