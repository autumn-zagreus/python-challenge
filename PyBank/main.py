# main.py of PyBank
# import os and csv so you can read paths and csv files
import os
import csv

# write down the path of the csv file so the computer knows where to look
budgetDataPath = os.path.join('Resources', 'budget_data.csv')
# Resources is the name of the folder we want to enter after that
# budget_data.csv is the name of the file we want
# print(budgetDataPath)
# check path using the above print line

# make a file to hold the output from this script
budgetAnalysisFile = os.path.join("budgetAnalysis.txt")

#variables
totalMonths = 0 # initialize the total amount of months to 0
total = 0 # total revenue value
change = [] # list value to hold each change
averageChange = 0 # average value of the numbers in the above list
months= [] # empty list to hold the months of each row

# read the file
with open(budgetDataPath) as budgetData:
    # create a csv reader object
    csvreader = csv.reader(budgetData)

    # read the header row
    header = next(csvreader)
    # move to first row
    firstRow = next(csvreader)

    # increment count of totalMonths
    totalMonths += 1

    # add onto total
    total += float(firstRow[1]) # all the numbers in budget_data.csv are ints, but we'll have to take an average later, so use floats
    # establish value of previous month's net - rev is index 1
    prevRev = float(firstRow[1])

    for row in csvreader:
        # increment count of totalMonths
        totalMonths += 1

        # add onto total
        total += float(row[1]) # all the numbers in budget_data.csv are ints, but we'll have to take an average later, so use floats

        # find net change
        netChange = float(row[1]) - prevRev
        # add this value onto the list of changes
        change.append(netChange)

        months.append(row[0])

        # update previous revenue
        prevRev = float(row[1])

# calculate average change
averageChange = sum(change)/len(change)

greatestIncrease = [months[0],change[0]] # greatest increase change value
greatestDecrease = [months[0],change[0]] # greatest decrease change value

for c in range(len(change)):
    #print(c)
    # calculate greatest increase and decrease
    if (change[c] > greatestIncrease[1]):
        # if val greater than original greatest increase, then new greatest increase is val
        greatestIncrease[1] = change[c]
        # update month
        greatestIncrease[0] = months[c]

    if (change[c] < greatestDecrease[1]):
        # if val less than original greatest decrease, then new greatest decrease is val
        greatestDecrease[1] = change[c]
        # update month
        greatestDecrease[0] = months[c]


output1 = ("Financial Analysis \n"
            + "-----------------------------------------------------------\n"
            + f"Total Months: {totalMonths}\n"
            + f"Total: ${total:,.2f}\n"
            + f"Average Change: {averageChange:,.2f}\n"
            + f"Greatest Increase in Profits: {greatestIncrease[0]}, Amount ${greatestIncrease[1]:,.2f}\n"
            + f"Greatest Decrease in Profits: {greatestDecrease[0]}, Amount ${greatestDecrease[1]:,.2f}")
print(output1) # outputs to terminal
with open(budgetAnalysisFile, "w") as outputFile:
    outputFile.write(output1)