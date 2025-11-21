import numpy as np
ar1 = np.array([1,2,3,4,5,6,7,8,9,10])
ar2 = np.array([[2,4,6,8], [1,3,5,7], [11,22,33,44], [10,20,30,40]])

print(ar1[2:9])
print(ar1[0:10:2])
print(ar1[1:8:3])

print(ar2[0])
print(ar2[0:2])
print(ar2[0:3:2])
print(ar2[:,0:2])
print(ar2[0:2,2:])
print(ar2[1::2,1::2])