import pandas as pd

data = {
    "Employees" : ["A1", "A2", "A3" , "A4", "A5"],
    "Salary" : [10000,15000,None,9000,12000],
    "Working for years" : [2,3,1,4,None]
}

df = pd.DataFrame(data)

print("Initial Dataframe: ")
print(df)

print("Columns with null Value Count: ")
print(df.isnull().sum())

# Drop missing Values:
# df.dropna(axis=0, inplace = True)

#Replacing Missing Values: 
# df.fillna(0, inplace=True)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print("Filled mean value to salary missing values: ")
# print(df)

print("Updated DataFrame: ")
print(df)





                   
                   