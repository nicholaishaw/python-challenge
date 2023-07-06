import os
import csv
import pandas as pd

#Creates the path for both of the CSV files
pybank_csv = os.path.join("starter_code", "pybank", "Resources", "budget_data.csv")
pypoll_csv = os.path.join("starter_code", "pypoll", "Resources", "election_data.csv")

#Sets the net_total variable to 0
net_total = 0

#Opens the csv files, creates a header, and the next function allows the code to be read after the header
#Tutor Marc Calache assisted with the development of lines # 
with open(pybank_csv) as csvfile:
    pybank = csv.reader(csvfile)
    header = next(pybank)
    Month_Count = 0
    for row in pybank:
        Month_Count = Month_Count + 1
        net_total += int(row[1])
        average_change = net_total/len(row[1])
        if row [1] > row [1] + 1
            greatest_increase = row
        elif row [1] < row [1] + 1
            greatest_decrease = row
    print(f"Average Change: {average_change}")
    print(f"Total Months: {Month_Count}")
    print(f"Net Total: {net_total}")

#Opens the pypoll csv file and iterates through each row
with open(pypoll_csv) as csvfile:
    pypoll = csv.reader(csvfile)
    header = next(pypoll)
    for row in pypoll:
        Total_votes += int(row[1])
print(f"Net Total: {total_votes}")
