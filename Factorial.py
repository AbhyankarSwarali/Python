# n=int(input("Enter a number "))
# fact=1

# for count in range(1, n+1):
#     fact=fact*count     #It is the repeating statement
# print("Factorial of",n, 'is',fact)


def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))