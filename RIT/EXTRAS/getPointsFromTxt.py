import csv

# Open the text file for reading and the CSV file for writing
with open('MAIN/picked_points.txt', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=' ')
    writer = csv.writer(outfile)

    # Loop over each row in the text file
    for row in reader:
        # Write each value to a separate column in the CSV file
        writer.writerow(row)
