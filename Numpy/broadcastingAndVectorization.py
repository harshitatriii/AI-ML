import numpy as np

# broadcasting:  A mechanism that allows NumPy to perform mathematical operations on arrays with different shapes.
# It automatically "expands" a smaller array to match the shape of a larger one.
# three rules of broadcasting:
# matching dimensions, expanding single elements, and incompatible shapes (which cause an error).

# 1 : matching dimensions: 

arr1 = np.array([100,200,300])

arr2 = np.array([5,6,7])

print(arr1 + arr2)


# whole array arithmetic operation: 

print(arr1 + 100)

print(arr1 * 2)

print("80 % of arr1 : " , (arr1/100)*80 )

# dimensions not matching: throws error: 

# arr3 = np.array([1,2,3,4])
# arr4 = np.array([1,2,3])

# print(arr3+arr4)