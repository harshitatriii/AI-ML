import numpy as np

arrInt = np.array([10,20,30,40,50,200])

print("Numpy Array: ", arrInt)

print("sum: " , np.sum(arrInt))
print("mean: " ,np.mean(arrInt))
print("max: ", np.max(arrInt))
print("min: ", np.min(arrInt))
print("covariance: ", np.var(arrInt))
print("Standard Deviation: ", np.std(arrInt))

# Indexing and Slicing

print("Indexing and Slincing: ")

print(arrInt[3]) # print index 3 of the array
print(arrInt[0:3:2]) # 0 included, 3 excluded, increase index by 2
print(arrInt[::2]) # 2 is what the index increases with rather than one by one 
print(arrInt[arrInt > 20]) # boolean mmasking: filtering elements based on conditions

print("array reshaped :")
print(arrInt.reshape(2,3)) # returns new array reshaped, keeps original intact

print(arrInt)

