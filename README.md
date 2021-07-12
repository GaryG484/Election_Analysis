# Election Analysis

## Overview

##### I extracted raw data from a Comma Separated Values (CVS) file and created code that would break down election data into three things based on the candidates and counties: how many votes were received, what percentage of the vote was received, and received the most votes. I parsed through the data and exported it to a text file for ease of reading. This will help us quickly see who won the election and by how much. It also shows which counties were most important for campaigning. 


## Election-Audit Results

##### This code takes the number of votes cast for each candidate in the separate counties and calculates how many each candidate received. It will also tell you what percentage of the vote each candidate received. It will then announce it and push the data to a text file.  The following information was pushed to the text file:
* There was a total of 369, 711 votes cast in this congressional election.
* Number of votes cast in each county:
  * Jefferson: 10.5% of the vote for a total of 38,855 votes.
  * Denver: 82.8% of the vote for a total of 306,055 votes.
  * Arapahoe: 6.7% of the vote for a total of 24,801 votes. 
* Denver had the largest number of votes.
* Number of votes cast for each candidate:
  * Charles Casper Stockham: 23% of the vote for a total of 85,213 votes.
  * Diana DeGette: 73.8% of the vote for a total of 272,892 votes.
  * Raymon Anthony Doane: 3.1% of the vote for a total of 11,606 votes. 
* Diana DeGette won the election with 73.8% of the vote for a total of 272,892 votes. 
## Election-Audit Summary

##### With this code it would only take slight modification to change the counties it looks at to another state for a different election. It can be used to look at past election data to strategize on which counties a candidate should focus their campaigns on.  It can also be modified to look at other types of data such as a new disease spreading or how many children are being born in each county. Below is an example of what the counties will look like once they are pushed to a text file. 
