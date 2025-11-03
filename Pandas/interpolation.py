import pandas as pd

data = {
    "Employees" : ["A1", "A2", "A3" , "A4", "A5"],
    "Salary" : [10000,15000,None,9000,12000],
    "Working for years" : [2,3,1,4,None]
}

df = pd.DataFrame(data)

df["Salary"].interpolate(type="linear", inplace=True)


print("Entering missing value's data using interpolation")
print (df)

# Read more about Interpolation and its various types and how the math works behind it to find the approximate value.
