import copy
c = copy

# Shallow copy
L = [10,20,30,40,50]
L1 = c.copy(L)
print(L1)
print(id(L))
print(id(L1))
print(id(L[0]))
print(id(L1[0]))

# Deep copy
class Person:
    def __init__(self,name):
        self.name = name

L = [Person("John"), Person("Tim"), Person("Jim")]
L1 = c.deepcopy(L)
print(L1)
print(id(L[0]))
print(id(L1[0]))
print(id(L) == id(L1))