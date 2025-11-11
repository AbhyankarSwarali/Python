from collections import Counter
L = ['Mark', 'Johny', 'David', 'Mark', 'Johny', 'Mark', 'James', 'Mathew']
c = Counter(L)

print(c)
print(c['Mark'])
print(c['Johny'])
print(c['David'])