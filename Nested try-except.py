L=[1,2,3,4,5]

try:
    try:
        index=int(input('Enter index no.: '))
    except ValueError as v:
        print(v)

    print(L[index])
except IndexError as i:
    print(i)
except Exception as e:
    print(e)