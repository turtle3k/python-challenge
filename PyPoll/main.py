#The Uncle Cleetus vote counting program
#import required modules
import os
import csv

# Path to collect data file from the Resources folder
electionData_csv = os.path.join('Resources', 'election_data.csv')

# Set variables here - FYI data file has Voter ID, County, and Candidate. 
crook = ""				#Each candidate/crook
vote_total = 0          #Total number of votes cast
vote_count_lib = {}		#Library to store each crook name and respective vote count
votes = 0				#Counter for number of votes
crook_percent_lib = {}	#Library to store each crooks percentage of votes
most_votes = 0			#Counter for the greatest number of votes - i.e. winner
grand_poohbah = ""		#The new Grand Poohbah.  Winner.  Big Cheese.

# Read in the CSV file
with open(electionData_csv, newline='', encoding='utf-8') as csvfile:

	# Split the data on commas and accommodate the header row
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
   
    # Loop through the data to acquire candidates (crooks) & count votes
	for row in csvreader:
		vote_total += +1
		crook = row[2]
		#if the crook is already listed, add 1 to his/her vote count
		if crook in vote_count_lib:
			vote_count_lib[crook] += +1
		else:
		    #if the crook is not listed, then add them to the list with an initial 1 vote
			vote_count_lib[crook] = 1
	

# Data is in, get % for each crook,err candidate and figure out the winner
for crook, votes in vote_count_lib.items():
	crook_percent_lib[crook] = '{0:.3%}'.format(votes / vote_total)
	if votes > most_votes:
		most_votes = votes
		grand_poohbah = crook
		
# Print/write out the results to terminal
print(f'Election Results')
print(f'{"-" * 31}')
print(f'Total Votes: {vote_total}')
print(f'{"-" * 31}')
for crook, votes in vote_count_lib.items():
	print(f'{crook:10}: {crook_percent_lib[crook]:>7}  ({votes:>7})')  
	#note formatting :10 and :>7 where numbers are column width and > is right justify
print(f'{"-" * 31}')
print(f'Winner: {grand_poohbah}')
print(f'{"-" * 31}')

# Print/write results to a text file
writefile = open('electionResults.txt' , 'w')
writefile.write('Election Results\n')
writefile.write(f'{"-" * 31} \n')
writefile.write(f'Total Votes: {vote_total}\n')
writefile.write(f'{"-" * 31} \n')
for crook, votes in vote_count_lib.items():
	writefile.write(f'{crook:10}: {crook_percent_lib[crook]:>7}  ({votes:>7}) \n')
writefile.write(f'{"-" * 31} \n')
writefile.write(f'Winner: {grand_poohbah} \n')
writefile.write(f'{"-" * 31} \n')	
writefile.close()	
