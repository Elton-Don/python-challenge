import os
import csv

budget_csv = os.path.join(".", "budget_data.csv")


# Read the csv and convert it into a list of dictionaries
with open(budget_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    # use next to skip first title row in csv file
    next(csvreader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_chg.append(revenue[i] - revenue[i-1])   
        avg_rev_chg = sum(rev_chg)/len(rev_chg)

        max_rev_chg = max(rev_chg)

        min_rev_chg = min(rev_chg)

        max_rev_chg_date = str(date[rev_chg.index(max(rev_chg))])
        min_rev_chg_date = str(date[rev_chg.index(min(rev_chg))])


    print("Avereage Revenue Change: $", round(avg_rev_chg))
    print("Greatest Increase in Revenue:", max_rev_chg_date,"($", max_rev_chg,")")
    print("Greatest Decrease in Revenue:", min_rev_chg_date,"($", min_rev_chg,")")