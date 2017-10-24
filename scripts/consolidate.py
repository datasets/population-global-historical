# Consolidate different population estimates into one single average value for
# each year
import csv
infile = file('data.csv')
outfile = file('out.csv', 'w')
reader = csv.reader(infile)
writer = csv.writer(outfile)
outrows = []

def avgpop(row):
    total = 0.0
    numnonzero = 0
    for col in row[2:]:
        if col:
            numnonzero += 1
            total += float(col)
    return total/numnonzero

count = 0
for row in reader:
    if count != 0: # have header
        # consolidated column is column 1 (remember start at 0)
        row[1] = avgpop(row)
    outrows.append(row)
    count += 1

writer.writerows(outrows)
