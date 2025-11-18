import csv

f = open('Employees.csv', 'r')
csv_reader = csv.reader(f)
print(csv_reader) 
next(csv_reader)
sals = []

for row in csv_reader:
    # print(row)
    # print(row[2])
    # print(int(row[2]))
    sals.append(int(row[2]))

f.close()

print(sals)
print('Minimum salary:', min(sals))
print('Maximum salary:', max(sals))

# prints object of csv reader here
# run the program in cmd