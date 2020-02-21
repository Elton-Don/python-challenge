import os
import csv

budget_csv = os.path.join(".", "budget_data.csv")


# Read and separate csv file
with open(budget_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    # use next to skip csv file header row
    next(csvreader) 
    #defining variables
    revenue = []
    date = []
    rev_chg = []

    # this loop sums revenue in csv file and counts total months
    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all rows of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_chg.append(revenue[i] - revenue[i-1])   
        avg_rev_chg = sum(rev_chg)/len(rev_chg)
        max_rev_chg = max(rev_chg)
        min_rev_chg = min(rev_chg)
        max_rev_chg_date = str(date[rev_chg.index(max(rev_chg))])
        min_rev_chg_date = str(date[rev_chg.index(min(rev_chg))])
    print("Avg Revenue Chg: $", round(avg_rev_chg))
    print("Greatest Inc. in Revenue:", max_rev_chg_date,"($", max_rev_chg,")")
    print("Greatest Dec. in Revenue:", min_rev_chg_date,"($", min_rev_chg,")")
    print(len(revenue))