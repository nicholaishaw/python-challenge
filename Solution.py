#Tutor Mark Fullton assisted with the development of the logic an syntax of the code in this document

import os
import csv

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

    print('Financial Analysis')
    print('------------')
    print(f'Total Months: {Month_Count}')
    print(f'Net Total: {profits_sum}')
    print(f'Average Change: {mean}')
    print(f'Greatest Increase: {greatest_increase} (${max_value})')
    print(f'Greatest Decrease: {greatest_decrease} (${min_value})')
    print('------------')
    print('')

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

print('Election Results')
print('------------')
print(f'Total Votes: {total_votes}')
print('------------')
for candidate in candidate_dic:
    candidate_votes = candidate_dic[candidate]
    candidate_percentage = (candidate_votes / total_votes) * 100
    print(f'{candidate}: {candidate_percentage}% ({candidate_votes})')

    if candidate_votes > comparison_votes:
        comparison_votes = candidate_votes
        winner = candidate

print('------------')
print(f'Winner: {winner}')