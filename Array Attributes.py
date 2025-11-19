import numpy as np

ar1 = np.array([1,3,5,7,9])
ar2 = np.array([[1,2,3], [4,5,6]])
ar3 = np.array([[[1,1], [2,2]], [[3,3], [4,4]]])
ar4 = np.array([1,2,3,4], ndmin=4)
ar5 = np.array([1.1,2.2,3.3])

print(ar1.ndim)
print(ar3.ndim)
print(ar3.shape)
print(ar4.shape)
print(ar2.dtype)
print(ar5.dtype)
print(ar2.itemsize)
print(ar1.nbytes)