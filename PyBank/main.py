#import required modules
import os
import csv

# Path to collect data from the Resources folder
budgetData_csv = os.path.join('Resources', 'budget_data.csv')

# Set lists for the date, and profit or loss data
date = []
date.clear()
porl = []
porl.clear()

# Read in the CSV file
with open(budgetData_csv, newline='', encoding='utf-8') as csvfile:

    # Split the data on commas and make note of the header row
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    # Loop through the data
    for row in csvreader:
        #print(int(row[1]))
        date.append(row[0])
        #print(date)
	    #porl.append(int(row[1]))
        porl.append(int(row[1]))
        
print(porl)
		
# Data is all in, start reporting
ttl_months = len(date)

ttl_porl = 0
gr_incr = porl[0]
print(type(gr_incr))
gr_decr = porl[0]
print(gr_decr)

for row in range(len(porl)):
    if porl[row] >= gr_incr:
	    gr_incr = porl[row]
	    gr_incr_mo = date[row]
    elif porl[row] <= gr_decr:
	    gr_decr = porl[row]
	    gr_decr_mo = date[row]
    ttl_porl += porl[row]
	
avg_chg = round(ttl_porl/ttl_months, 2)

# Print the results
print("Financial Analysis")
print("-" * 45)
print("Total Months: " + str(ttl_months))
print("Total: $" + str(ttl_porl))
print("Average Change: " + str(avg_chg))
print("Greatest Increase in Profits: " + gr_incr_mo + "  " + str(gr_incr))
print("Greatest Decrease in Profits: " + gr_decr_mo + "  " + str(gr_decr))

# Write the results to a file
