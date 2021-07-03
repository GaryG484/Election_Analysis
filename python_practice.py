print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]

#dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#If-Else
if "El Paso" in counties:
    print("El Pas is in the list of counties")
else:
    print("El Paso is not the list of counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Pas are not in the list of counties.")

#for loops
for county in counties:
    print(county)

#Key Method
for county in counties_dict.keys():
    print(county)

#get the values of a dictionary 
for voters in counties_dict.values():
    print(voters)

#get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Get the values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#f strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#practice with f strings
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#multiple f strings practice
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
                                                    #:.2f makes the number go out to two decimal places
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#using open to read from a file, direct path. WOuld need to import the file first
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Assign a variable for the file to load and the path. This is direct path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
# with doesnt require you to close the file, whereas open alone would.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

 # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file
    for row in file_reader:
        print (row)
    print(election_data)
