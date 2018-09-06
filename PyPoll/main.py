import csv
import locale
import sys

locale.setlocale(locale.LC_ALL,'')

csvpath = 'election_data.csv'

with open(csvpath, 'r', newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
   
    voter = []
    cand = []

    for row in csvreader:
        voter.append(row[0])
        cand.append(row[2])
    
    total = len(voter)
    unique_cand = list(set(cand))
    tally = []
    pct = []

    for name in unique_cand:
        x = cand.count(name)
        tally.append(x)
        pct.append("{:.2%}".format(x/total))

    # tally = [[name,cand.count(name),"{:.2%}".format(cand.count(name)/total)] for name in set(cand)]

    winner = tally.index(max(tally))

def output():
    print("Election Results")
    print("----------------------------------------")
    print(f"Total Votes: {total}")
    print("----------------------------------------")
    for y in range(len(unique_cand)):
        print(f"{unique_cand[y]}: {pct[y]} ({tally[y]})")
    print("----------------------------------------")
    print(f"Winner: {unique_cand[winner]}")
    print("----------------------------------------")

output()

output_path = 'election_results.txt'

with open(output_path, 'w') as output_file:
    sys.stdout = output_file
    output()