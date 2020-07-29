#import os
import os

##how do you read csvs?
import csv

#path to collect data from Resources folder
csvpath = os.path.join('.','Resources','budget_data.csv')

#month counter variable
total_months = 0

#pl count variable
total_pl = 0

with open(csvpath) as csvfile:
    reader_bank = csv.reader(csvfile, delimiter = ",")

    header = next(reader_bank)

    for row in reader_bank:
        total_months = (total_months + 1)

    for row in reader_bank:
        sum(total_pl+1)
 
    #print total_months
    print (total_months)
    
    #print total_pl
    print (total_pl)
