import csv
import numpy
import locale
import sys

locale.setlocale(locale.LC_ALL,'')

csvpath = 'budget_data.csv'

with open(csvpath, 'r', newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
   
    months = []
    pnl = []
    
    for row in csvreader:
        months.append(row[0])
        pnl.append(float(row[1]))

    change = [y-x for x,y in zip(pnl,pnl[1:])]
    maxchange = change.index(max(change))
    minchange = change.index(min(change))

def output():
    print("Financial Analysis")
    print("--------------------------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total P&L: {locale.currency(sum(pnl), grouping=True)}")
    print(f"Average M/M Change: {locale.currency(numpy.mean(change), grouping=True)}")
    print(f"Greatest M/M Increase in P&L: {months[maxchange+1]}, {locale.currency(change[maxchange], grouping=True)}")
    print(f"Greatest M/M Decrease in P&L: {months[minchange+1]}, {locale.currency(change[minchange], grouping=True)}")

output()

output_path = 'financial_analysis.txt'

with open(output_path, 'w') as output_file:
    sys.stdout = output_file
    output()