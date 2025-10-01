num = 1234
N = num
result = 0
while N > 0:
    lst_dig = N % 10
    result = result*10 + lst_dig

print(result)
