import numpy as np

# 1-D Array
ar1 = np.array(12)
# ar2 = np.array(1,2,3,4,5)
# Shows TypeError: array() takes from 1 to 2 positional arguments but 5 were given
ar3 = np.array([1,2,3,4,5])
ar4 = np.array((1,3,5,7,9))

# 2-D Array
arr1 = np.array([[1,3,5,7], [2,4,6,8]])
arr2 = np.array(((1,2,3), (4,5,6)))

# 3-D Array
Arr1 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])