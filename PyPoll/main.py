#Uncle Cleetus vote counting code
#import required modules
import os
import csv

# Path to collect data file from the Resources folder
electionData_csv = os.path.join('Resources', 'election_data.csv')

# Set variables here - rem data file has Voter ID, County, and Candidate. 
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
		#vote_total += +1
		vote_total = vote_total + 1
		crook = row[2]
		if crook in vote_count_lib:
			#vote_count_lib[crook] += +1
			vote_count_lib[crook] = vote_count_lib[crook] + 1
		else:
			vote_count_lib[crook] = 1
	
			

# Data is in, get % for each crook,err candidate and figure out the winner
# vote_total = len(vote_count_lib) - calculating above - take out above & use this??
# print(vote_total)  #Used as quick ck - file importing, counting rows/votes
for crook, votes in vote_count_lib.items():
	crook_percent_lib[crook] = '{0:.0%}'.format(votes / vote_total)
	if votes > most_votes:
		most_votes = votes
		grand_poohbah = crook
		
# Print/write out the results to terminal
print(f'Election Results')
print(f'{"-" * 29}')
print(f'Total Votes: {vote_total}')
print(f'{"-" * 29}')
for crook, votes in vote_count_lib.items():
	print(f'{crook:10}: {crook_percent_lib[crook]:6}  ({votes})')  
	#note the :10 and :6 are formatting - i.e. amount of spaces so the columns line up better
print(f'{"-" * 29}')
print(f'Winner: {grand_poohbah}')
print(f'{"-" * 29}')

# Print/write results to a text file
#electionResults_txt = os.path.join('Resources', 'election_results.txt')
#with open(electionResults_txt, "w", newline="") as text:
#	writer.writerow[
#electionResults_txt = os.path.join('Resources', 'election_results.txt')
writefile = open('electionResults.txt' , 'w')
writefile.write('Election Results\n')
writefile.write(f'{"-" * 29} \n')
writefile.write(f'Total Votes: {vote_total}\n')
writefile.write(f'{"-" * 29} \n')
for crook, votes in vote_count_lib.items():
	writefile.write(f'{crook:10}: {crook_percent_lib[crook]:6}  ({votes}) \n')
writefile.write(f'{"-" * 29} \n')
writefile.write(f'Winner: {grand_poohbah} \n')
writefile.write(f'{"-" * 29} \n')	
writefile.close()	
