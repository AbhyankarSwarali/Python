Alex = int(input("Alex age: "))
Brain = int(input("Brain age: "))
Chandler = int(input("Chandler age: "))

if Alex > Brain and Alex > Chandler:
    print("Alex is the eldest")
elif Brain > Chandler:
    print("Brain is the eldest")
else:
    print("Chandler is the eldest")
