#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
import os
import csv

budget_csv = os.path.join(".", "election_data.csv")

votes =[]
Candidate = []
vote_pcnt = []
vote_cnt = 0
vote_cnti = 0
# Read the csv and convert it into a list of dictionaries
with open(budget_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    next(csvreader) 
    for row in csvreader:
      vote_cnt = vote_cnt + 1
      if row[2] not in Candidate:
        Candidate.append(row[2])
    print("Candidate Names", (Candidate))  
    print("Votes Cast:", (vote_cnt))
    print("# of candidates", len(Candidate))
    

for x in range(0,len(Candidate)):
  with open(budget_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    next(csvreader) 
    vote_cnti = 0       
    for row in csvreader:
      if row[2] == Candidate[x]:
        vote_cnti = vote_cnti + 1
  votes.append(vote_cnti)
  vote_pcnt.append(vote_cnti/vote_cnt)
print(Candidate)  
print(votes)
print(vote_pcnt)
    

        

