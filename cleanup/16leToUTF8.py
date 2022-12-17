import os

# ------------------------------------------ #
#  convert from UTF-16-LE to UTF-8 bom       #
# ------------------------------------------ #
directory = 'C:/Users/ripny/Desktop/compccrs/src/'
output_directory = "C:/Users/ripny/Desktop/compccrs/dest/"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    with open(f, 'rb') as source_file:
        with open(os.path.join(output_directory,filename), "w+b") as dest_file:
            contents= source_file.read()
            dest_file.write(contents.decode('utf-16-le').encode('utf-8'))