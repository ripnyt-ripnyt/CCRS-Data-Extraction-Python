import csv

# Open the input CSV file for reading
with open('input.csv', 'r') as f_in:
    # Create a CSV reader object
    reader = csv.reader(f_in)
    
    # Skip the first 46121363 rows
    for _ in range(121363):
        next(reader)
    
    # Open the output CSV file for writing
    with open('output.csv', 'w', newline='') as f_out:
        # Create a CSV writer object
        writer = csv.writer(f_out)
        
        # Write the remaining rows to the output file
        for row in reader:
            writer.writerow(row)
