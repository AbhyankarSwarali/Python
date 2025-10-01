n = int(input("Enter a number: "))
num = n
while num > 0:
    last_dig = num %10
    print(last_dig, end=' ')
    num = num // 10