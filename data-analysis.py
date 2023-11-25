#PyBank analysis:

#Importing dependencies
import os
import csv

#Create a text document that will hold the results of the PyBank analyses
results_pybank_path = 'results-PyBank.txt'
results_pybank = open(results_pybank_path, 'w')

#Create a path to the csv file holding the budget data
pybank_csv = os.path.join('PyBank', 'budget_data.csv')

#Initialize 'previous' to 0
previous = 0

#Open and read the csv file and skip the header
with open(pybank_csv) as csvfile:
    pybank = csv.reader(csvfile)
    header = next(pybank)

    #Create lists to hold the profts, months, and the month differences
    months = []
    profits = []
    profit_loss_differences = []

    #Initialize the month count to 0
    Month_Count = 0

    #Iterate through the budget data csv file to 
    for row in pybank:

        #Put each month into the months list
        months.append(row[0])

        #Put the profits/loses into the profits list
        profits.append(int(row[1]))

        #Use the month_count variable to keep count of the months in the iteration
        Month_Count = Month_Count + 1

        #Since one of our goals is to find the difference in the businesses' profits and loses each month, the very first month of profits in the.\
        #dataset cannot be subtracted with anything. As such, the "difference" would effectively be 0. This IF statement states that if it's the.\
        #first month, 0 will be the difference in profits.
        if Month_Count == 1:
            profit_loss_differences.append(0)
        else:
            #Obtain the difference of the current row with the previous row and put it in 'profit_loss_differences' list
            Difference = int(row[1]) - previous
            profit_loss_differences.append(Difference)

        #Obtain the profits in the previous row's
        previous = int(row[1])

    #Get the sum, average, maximum, and minmum of the dataset
    profits_sum = sum(profits)
    mean = sum(profit_loss_differences)/(len(profit_loss_differences)-1)
    max_value = max(profit_loss_differences)
    min_value = min(profit_loss_differences)

    #Get the indexes to find the months with the greatest increase and greatest decrease
    max_index = profit_loss_differences.index(max(profit_loss_differences))
    min_index = profit_loss_differences.index(min(profit_loss_differences))
    greatest_increase = months[max_index]
    greatest_decrease = months[min_index]

#Print the results in the text file ('results-pybank.txt')
print('Financial Analysis', file=results_pybank)
print('------------', file=results_pybank)
print(f'Total Months: {Month_Count}', file=results_pybank)
print(f'Net Total: ${profits_sum}', file=results_pybank)
print(f'Average Change: ${mean}', file=results_pybank)
print(f'Greatest Increase: {greatest_increase} (${max_value})', file=results_pybank)
print(f'Greatest Decrease: {greatest_decrease} (${min_value})', file=results_pybank)
print('------------', file=results_pybank)
results_pybank.close()


#--------------------
# PyPoll Analysis:

#Create a text document that will hold the results of the PyPoll analyses
results_pypoll_path = 'results-Pypoll.txt'
results_pypoll = open(results_pypoll_path, 'w')

#Create a path to the csv file holding the poll data
pypoll_csv = os.path.join('PyPoll', 'election_data.csv')

#Initialize the total votes and comparison votes to 0
total_votes = 0
comparison_votes = 0

#Create a dictionary to store the candidate information in
candidate_dic = {}

#Open the csv file and skip the header
with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)

    #Loop through the csv document and store each candidate and each time they were voted for in the dictionary 
    for row in csv_reader:
        candidate = row[2]
        if candidate in candidate_dic:
            candidate_dic[candidate] = candidate_dic[candidate] + 1
        else:
            candidate_dic[candidate] = 1
        
        #Get the total number votes
        total_votes = total_votes + 1

#Print the results
print('Election Results', file=results_pypoll)
print('------------', file=results_pypoll)
print(f'Total Votes: {total_votes}', file=results_pypoll)
print('------------', file=results_pypoll)

#Loop through the candidate dictionary to get the percentage of votes for each candidate as well as the candidate with the most votes
for candidate in candidate_dic:
    candidate_votes = candidate_dic[candidate]
    candidate_percentage = (candidate_votes / total_votes) * 100

    #Print the result
    print(f'{candidate}: {candidate_percentage}% ({candidate_votes})', file=results_pypoll)

    #Obtain the winning candidate
    if candidate_votes > comparison_votes:
        comparison_votes = candidate_votes
        winner = candidate

#Print the winner
print('------------', file=results_pypoll)
print(f'Winner: {winner}', file=results_pypoll)
print('------------', file=results_pypoll)
results_pypoll.close()