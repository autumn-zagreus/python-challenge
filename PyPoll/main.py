import os
import csv

dataFile = os.path.join("Resources/election_data.csv")
#print(dataFile)
pollAnalysisFile = os.path.join("pollAnalysis.txt")

# create variables
numVotes = 0 # holds total number of votes
counties = [] # list to hold the county name for each ID number
candidates = [] # list to hold the candidate voted for by each ID number
candidateVotes = {} # dictionary to hold how many votes each candidate receives
winCount = 0 # holds the winning count
winCandidate = "" # holds the name of the winning candidate

# read the csv file
with open(dataFile) as pollData:
    # create csv reader
    csvreader = csv.reader(pollData)

    header = next(csvreader)

    # rows are going to be lists
        # index 0 is Ballot ID
        # index 1 is County name
        # index 2 is Candidate name

    for row in csvreader:
        numVotes += 1

        # check to see if the candidate voted for is in the current list of candidates
        if row[2] not in candidates:
            # if the candidate's name is not in the current list of candidates,
            # add it in - append
            candidates.append(row[2])

            # add the value to the dictionary as well
            # { "key": value}
            # start the count at 1 for the votes
            candidateVotes[row[2]] = 1
        
        else:
            # the candidate's name is on the current list of candidates
            # add a vote to that candidate's count
            candidateVotes[row[2]] += 1
#print(candidateVotes)
voteOutput = ""
for candidate in candidateVotes:
    # retrieve vote count and percentage for each candidate
    votes = candidateVotes.get(candidate)
    #print(votes)
    votePercent = (float(votes)/float(numVotes)) * 100.00

    voteOutput += f"{candidate}: {votePercent:,.2f}% ({votes})\n"

    # compare votes to winning count
    if votes > winCount:
        # update winCount
        winCount = votes
        # update winCandidate
        winCandidate = candidate


# output needs to print both to the terminal and to a txt file
output = ("Election Results\n"
            + "------------------------------\n"
            + f"Total Votes: {numVotes:,.2f}\n"
            + f"-----------------------------\n"
            + (voteOutput)
            + "------------------------------\n"
            + f"Winner: {winCandidate}\n"
            + "------------------------------")
print(output) # prints to terminal
with open(pollAnalysisFile, "w") as outputFile:
    outputFile.write(output)