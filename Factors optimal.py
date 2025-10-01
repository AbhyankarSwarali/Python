from math import sqrt
a = int(input("Enter a number: "))
factors = []
for i in range(1, int(sqrt(a)) + 1):
    if a % i == 0:
        factors.append(i)
        if a // i != i:
            factors.append(a//i)

print(sorted(factors))