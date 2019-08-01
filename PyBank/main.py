#import required modules
import os
import csv

# Path to collect data from the Resources folder
budgetData_csv = os.path.join('Resources', 'budget_data.csv')

# Set lists for the date, and profit or loss (porl) data.  Make sure they're empty
date = []
date.clear()
porl = []
porl.clear()

# Read in the CSV file
with open(budgetData_csv, newline='', encoding='utf-8') as csvfile:

    # Split the data on commas and accommodate the header row
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    # Loop through the data to put it into date and profit or loss lists
	# Cast PorL data as integer so we can use it for calculations later
    for row in csvreader:
        #print(int(row[1]))
        date.append(row[0])
        #print(date)
	    #porl.append(int(row[1]))
        porl.append(int(row[1]))

		
# Data is all in, set some variables 
ttl_porl = 0
gr_incr = 0
gr_decr = 0
porl_change = 0
porl_chg_list = []


# Run calculation to figure out greatest profit increase and greatest loss decrease
for row in range(len(porl)):
	ttl_porl += porl[row]
	porl_change = porl[row] - porl[row-1]
	porl_chg_list.append(porl_change) 
	if porl_change >= gr_incr:
		gr_incr = porl_change
		gr_incr_mo = date[row]
	elif porl_change <= gr_decr:
		gr_decr = porl_change
		gr_decr_mo = date[row]
		
ttl_months = len(date)
#avg_chg = round(sum(porl_chg_list)/ttl_months, 2)
#can't get porl_chg_list to sum.   what up??
#avg_chg = sum(porl_chg_list)
# print(porl_chg_list)
# avg_chg = sum(int(i) for i in porl_chg_list)
for i in porl_chg_list
	ttl_chg += porl_chg_list(i)

avg_chg = ttl_chg / ttl_months


# Print the results to terminal
print("Financial Analysis")
print("-" * 45)
print("Total Months: " + str(ttl_months))
print("Total: $" + str(ttl_porl))
print("Average Change: $" + str(avg_chg))
print("Greatest Increase in Profits: " + gr_incr_mo + "  $" + str(gr_incr))
print("Greatest Decrease in Profits: " + gr_decr_mo + "  $" + str(gr_decr))

# Write the results and export as a text file
