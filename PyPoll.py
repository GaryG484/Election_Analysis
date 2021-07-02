# The data we need to retrieve.

# This is necessary if wer are doing indirect paths. Adds our dependencies.
import csv
import os
# Assign a variable for the file to load and the path. This is indirect.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable  to write data on a file with an inderect path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.

# with doesnt require you to close the file, whereas open alone would.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print only the header row of the CSV file
    headers = next(file_reader)
    print (headers)
    print(election_data)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file. We're writing the counties. I could add comma and space to seperate the words. 
    txt_file.write("Arapahoe ")
    # \n is called a newline escape sequence and is what seperates the variables onto new lines.
    txt_file.write("\nDenver ")
    txt_file.write("\nJefferson ")



# 1. The total number of votes cast

# 2. A complete list of canidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote. 