# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("PyPoll_Analysis", "county_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# 2: Track the largest county and county voter turnout.
county_results = ""
largest_county_vote = 0
largest_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_results:
    reader = csv.reader(election_results)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


 # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    county_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        "County Votes")
    print(county_results)
 

    # Save the results to our text file part 2
    txt_file.write(county_results)
    

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:

        # Retrieve vote count and percentage
        votes = county_votes[county]


        # 6b: Retrieve the county vote count.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})")
        print(county_results)

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > largest_county_vote) and (vote_percentage > largest_county_percentage):

            # If true then set winning_count = votes and winning_percent = vote_percentage.
            largest_county_vote = votes
            largest_county_percentage = vote_percentage
            winning_county = county

    txt_file.write("\n")

    # 7: Print the county with the largest turnout to the terminal.
    county_results = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")

    print(county_results)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_results)


    # Save the final candidate vote count to the text file.
    for candidate in candidate_votes:

         # Retrieve vote count and percentage
        votes_candidate = candidate_votes[candidate]
        vote_percentage_candidate = float(votes_candidate) / float(total_votes) * 100

        # Print each candidate's voter count and percentage to the terminal.
        candidate_results = (
            f"{candidate}: {vote_percentage_candidate:.1f}% ({votes_candidate:,})\n")
        print(candidate_results)


        #  Save the candidate results to our text file.
        txt_file.write(county_results)
                

        # Determine winning vote count, winning percentage, and candidate.
        if(votes_candidate > winning_count) and (vote_percentage_candidate > winning_percentage):
            winning_count = votes_candidate
            winning_percentage = vote_percentage_candidate
            winning_candidate = candidate
        

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(county_results)

