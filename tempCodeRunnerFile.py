s = [1,1,2,3,3,3,4,6,2,7,5,6,1,6]
new = []

for i in s:
    if i not in new:
        new.append(i)

print(new)