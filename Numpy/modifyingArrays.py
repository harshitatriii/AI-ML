import numpy as np

arr = np.array(["10", "12" , 46])

print(arr)
print(arr.dtype)

arrInt = arr.astype("int")

print(arrInt)
print(arrInt.dtype)


print("Inserting element into an array: ")

newArray = np.insert(arr, 2, 100,0) # array ref, index, value, axis(1 or 0 , row or column) 
#"Insert adds elements into an new array only and returns that.
print("Insert adds elements into an new array only and returns that.")
print (newArray)
