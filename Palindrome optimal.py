num = int(input("Enter a number: "))
N = num
result = 0
while N > 0:
    lst_dig = N % 10
    result = result*10 + lst_dig

if result == num:
    print("Palindrome")
else: 
    print("Not a palindrome")