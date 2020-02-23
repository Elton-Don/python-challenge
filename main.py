import os
import csv

budget_csv = os.path.join(".", "election_data.csv")

votes =[]
Candidate = []
vote_pcnt = []
vote_cnt = 0
vote_cnti = 0
Winner =[]
winvote = 0
prow = []

# Read the csv and convert it into a list of dictionaries
with open(budget_csv, 'r') as csv_file:     # opening and reading the file
    csvreader = csv.reader(csv_file, delimiter=",")
    next(csvreader)      #skipping the header
    for row in csvreader:
      vote_cnt = vote_cnt + 1
      if row[2] not in Candidate:
        Candidate.append(row[2])
  

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

winvote = 0
for x in range(0,len(Candidate)):
  if (int(votes[x])) > winvote:
    winvote = int(votes[x])
    Winner = Candidate[x]


prows1 =[
    ["Election Results"], 
    ["------------------------"],    
    ["Total Votes:", (vote_cnt)],
    ["------------------------"],  
]

prows3 =[   
    ["------------------------"],    
    ["Winner:", Winner],
    ["------------------------"]     
]

#for x in range(0,len(Candidate)):
#  prow =[f"{Candidate[x]}, {vote_pcnt[x] :.3%}, {votes[x]}"]
#  print(prow)


for row in prows1:  
    print(row)  
for row in prows3:
    print(row)    
for x in range(0,len(Candidate)):
    print((f"{Candidate[x]}, {vote_pcnt[x] :.3%}, {votes[x]}"))


with open('election_results.csv', 'wt') as w:
  csv_writer = csv.writer(w)
  for row in prows1:
    csv_writer.writerow(row)
  for x in range(0,len(Candidate)):
    prow =[f"{Candidate[x]}, {vote_pcnt[x] :.3%}, {votes[x]}"]
    csv_writer.writerow(prow)
  for row in prows3:
    csv_writer.writerow(row)