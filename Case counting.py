def count(phrase):
    lower = 0
    upper = 0

    for x in phrase:
        if x.islower():
            lower += 1
        elif x.isupper():
            upper += 1

    return lower, upper

L = input("Enter a phrase: ")
print(count(L))