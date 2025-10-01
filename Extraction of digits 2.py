number = int(input("Enter a number: "))
n = number
count = 0
while n >0: 
    count += 1
    n = n // 10

print(count)