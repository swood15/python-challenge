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
    maxpnl = pnl.index(max(pnl))
    minpnl = pnl.index(min(pnl))

def output():
    print("Financial Analysis")
    print("--------------------------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total P&L: {locale.currency(sum(pnl), grouping=True)}")
    print(f"Average Monthly Change: {locale.currency(numpy.mean(change), grouping=True)}")
    # Greatest increase in profits refers to max(pnl) or max(change)?
    print(f"Greatest Increase in P&L: {months[maxpnl]}, {locale.currency(pnl[maxpnl], grouping=True)}")
    print(f"Greatest Decrease in P&L: {months[minpnl]}, {locale.currency(pnl[minpnl], grouping=True)}")

print(output())

output_path = 'financial_analysis.txt'

with open(output_path, 'w') as output_file:
    sys.stdout = output_file
    print(output())