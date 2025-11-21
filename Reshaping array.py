import numpy as np
ar = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(ar.shape)
print(ar.reshape(3,4))
print(ar.reshape(6,2))
print(ar.reshape(3,2,2))
print(ar.reshape(2,1,6))

print(ar.flatten()) # Converts any n-dimensional array into 1-dimensional array