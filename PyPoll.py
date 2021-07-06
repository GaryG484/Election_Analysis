# The data we need to retrieve.
# This is necessary if wer are doing indirect paths. Adds our dependencies.
import csv
import os
# Assign a variable for the file to load and the path. This is indirect.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable  to write data on a file with an inderect path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter for step 1 and set it equal to zero
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare an empty dictionay for number of votes per candidate
candidate_votes = {}

# Winning Candidate and WInning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
# with doesnt require you to close the file, whereas open alone would.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print only the header row of the CSV file
    headers = next(file_reader)

# 1. The total number of votes cast

    # Print each row in the CSV file. 
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

# 2. A complete list of canidates who received votes
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate. . .
        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #Save the results to our text file. 
        with open(file_to_save, "w") as txt_file:
            election_results = (
                #print the final vot count to the terminal
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
            print(election_results, end="")

            # Save the final vote cout to the text file.
            txt_file.write(election_results)

    # 3. The percentage of votes each candidate won

    # Determine the % of votes for each candidate by looping through the the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100


        with open(file_to_save, "a") as txt_file:
            candidate_results = (
 
                # Save the candidate results to our text file. 
                candidate_results) = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)

            # Save the candidate results to our text file.
            txt_file.write(candidate_results)

    # 4. The total number of votes each candidate won

        # Determine the winning vote count and candidate
        # Determine if the votes are greater than the winning count.
if (votes > winning_count) and (vote_percentage > winning_percentage):
    # If true then set winning_count = votes and winning_percent = vote_percentage
    winning_count = votes
    winning_percentage = vote_percentage
                
    # Set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name

    # 5. The winner of the election based on popular vote. 
    # results summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)