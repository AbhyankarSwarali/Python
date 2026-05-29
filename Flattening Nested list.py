def flatten(L):
    
    for x in L:
        if hasattr(x, '__iter__'):
            yield from flatten(x)
        else:
            yield x

f=flatten([1,2,[3,4,[5,6],7],8])

print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f), end=' ')
print(next(f))