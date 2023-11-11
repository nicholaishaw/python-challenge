#Tutors Marc Calache and Mark Fullton assisted with the development of the logic an syntax of the code in this document
#The idea to sum a row on lines #19-21 originated from a Stack Overflow thread (Link: https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python, the author is named Martijn Pieters, and the date of the publication is November 22, 2012).
#The syntax to export python results to a text file was provided from: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

import os
import csv

results_path = 'results.txt'
results = open(results_path)
pybank_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

net_total = 0


with open(pybank_csv) as csvfile:
    pybank = csv.reader(csvfile)
    header = next(pybank)
    month_variable = []
    profits = []
    PL_List = []
    Month_Count = 0

    for row in pybank:
        month_variable.append(row[0])
        profits.append(int(row[1]))
        Month_Count = Month_Count + 1
        net_total += int(row[1])
        if Month_Count == 1:
            PL_List.append(0)
        else:
            Difference = int(row[1]) - previous
            PL_List.append(Difference)
        previous = int(row[1])
        
    profits_sum = sum(profits)
    mean = sum(PL_List)/(len(PL_List)-1)
    max_profits = max(PL_List)
    max_index = PL_List.index(max(PL_List))
    min_index = PL_List.index(min(PL_List))
    max_value = max(PL_List)
    min_value = min(PL_List)
    greatest_increase = month_variable[max_index]
    greatest_decrease = month_variable[min_index]

    print('Financial Analysis', file=results)
    print('------------', file=results)
    print(f'Total Months: {Month_Count}', file=results)
    print(f'Net Total: {profits_sum}', file=results)
    print(f'Average Change: {mean}', file=results)
    print(f'Greatest Increase: {greatest_increase} (${max_value})', file=results)
    print(f'Greatest Decrease: {greatest_decrease} (${min_value})', file=results)
    print('------------', file=results)
    print('', file=results)
    print('', file=results)
    print('', file=results)

#--------------------

pypoll_csv = os.path.join('pypoll', 'Resources', 'election_data.csv')
total_votes = 0
comparison_votes = 0
candidate_dic = {}
with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    for row in csv_reader:
        candidate = row[2]
        if candidate in candidate_dic:
            candidate_dic[candidate] = candidate_dic[candidate] + 1
        else:
            candidate_dic[candidate] = 1
        total_votes = total_votes + 1

print('Election Results', file=results)
print('------------', file=results)
print(f'Total Votes: {total_votes}', file=results)
print('------------', file=results)
for candidate in candidate_dic:
    candidate_votes = candidate_dic[candidate]
    candidate_percentage = (candidate_votes / total_votes) * 100
    print(f'{candidate}: {candidate_percentage}% ({candidate_votes})', file=results)

    if candidate_votes > comparison_votes:
        comparison_votes = candidate_votes
        winner = candidate

print('------------', file=results)
print(f'Winner: {winner}', file=results)
print('------------', file=results)
results.close()
