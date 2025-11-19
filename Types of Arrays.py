import numpy as np

# Zeros
zero1 = np.zeros(3)
zero2 = np.zeros((3,4,5)) # 3 planes, 4 rows, 5 cols
print(zero1.dtype)
print(zero2.ndim)

# Ones
one1 = np.ones(5)
one2 = np.ones((3,3))
print(one1)
print(one2)

# Empty
empty = np.empty(7)
print(empty) #Write from idle

# Eye
eye1 = np.eye(4)
eye2 = np.eye(3,4)
print(eye1)
print(eye2)

# Diag
diag1 = np.diag([1,2,3])
diag2 = np.diag((1,3,5,7,9))
print(diag1)
print(diag2)

# Arange
ar1 = np.arange(1,6)
ar2 = np.arange(0,10,2)
ar3 = np.arange(0,6).reshape(2,3)
print(ar1)
print(ar2)
print(ar3)

# Linspace
ls1 = np.linspace(0,10,num=5)
ls2 = np.linspace(0,8,6).reshape(3,2)
print(ls1)
print(ls2)