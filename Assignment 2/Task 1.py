# Task 1
# By: Daniel Gallagher

#columns 5, 7, 3
# 7/3 * 100

#importing the module
import csv

#opening the file in read mode
filename = open('Sample for task 1 - separate column view.csv', 'r')

#creating the dictreader object
file = csv.DictReader(filename)

#creating empty lists
TotalPkAtTxNode = []
PkreceivedAtRxNode = []

# iterating over each row and append
# values to the empty lists
for col in file:
    #column 5
    TotalPkAtTxNode.append(col['Packets'])
    #column 7
    PkreceivedAtRxNode.append(col['Rx Packets'])

#dividing column 7 and column 3 and multiplying it by 100
result_list = []
for i in range(0, len(TotalPkAtTxNode)):
    result_list.append(PkreceivedAtRxNode[i] / TotalPkAtTxNode[i] * 100)

#printng the result list
print(str(result_list))






