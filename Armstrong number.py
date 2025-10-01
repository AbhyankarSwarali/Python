n = int(input("Enter a number: "))
x = n
nod = len(str(n))
total = 0
while x > 0:
    ld = x % 10
    total = total + ld**nod
    x = x // 10

if total == n:
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is not an Armstrong number')