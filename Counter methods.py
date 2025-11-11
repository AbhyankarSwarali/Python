from collections import Counter
L = ['Mark', 'Johny', 'David', 'Mark', 'Johny', 'Mark', 'James', 'Mathew']
c = Counter(L)

print(c)
print(c.get('Mark'))
print(c.keys())
print(c.values())
print(c.items())
c.update({'Alex':4})
print(c)

for i in c.elements():
    print(i)

print(c.pop('Alex'))
print(c.popitem())
print(c.most_common(1))
print(c.most_common(2))

d = c.copy()
print(d)
d.clear()
print(d)