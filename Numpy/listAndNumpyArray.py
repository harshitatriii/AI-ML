import numpy as np

# list = [1,2,3,4,5]

# print ("list : ",list)

# list_arr = np.array(list)
# print ("list converted to numpy array: " , list_arr)


# arr = np.array([1,2,3])
# print("numpy array : " ,arr)

zeroes = np.zeros((5)) 
ones = np.ones((2,3)) # give shape in tuple () 
filled_array = np.full(4,3)

print(zeroes)
print(ones)
print(filled_array)
arange = np.arange(1,10,2)
print(arange)

identity_array = np.eye(3,4)
print(identity_array)

