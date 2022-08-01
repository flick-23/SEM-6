import csv
rows = []
with open("Finds.csv") as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        rows.append(row)

hypothesis = rows[0]
attributes = len(rows[0])-1
print("Attributes : ", attributes)
for row in rows:
    print("ROW : ", row)
    for i in range(attributes):
        if row[attributes] == 'yes':
            if row[i] != hypothesis[i]:
                hypothesis[i] = '?'
print("Final hypothesis : ", hypothesis)
