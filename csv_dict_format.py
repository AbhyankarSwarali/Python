import csv
import pprint

f = open('Employees.csv', 'r', encoding='utf-8-sig')
rdr = csv.DictReader(f)
emps = {}

for row in rdr:
    # print(row)
    emps[row['Name']] = row


# print(emps)
pprint.pprint(emps)
# print('Harry:', emps['Harry'])
f.close()