import pandas as pd

data = {
    "Name": ["Harhsit" , "Rishabh", "Virat"],
    "Countries Visited" :[1,9,21],
    "Dont Need": [1,1,1]
}

df = pd.DataFrame(data)

print("new data Set: ")
print(df)

# Removing a column here: 

print("Remving some columns: ")
print(df.drop(columns=["Dont Need", "Name"]))

print("It doesnt delete from the original data but only returned a copy ")

print(df)

df.drop(columns=["Dont Need"] , inplace=True)

print("Permanently deleted some columns using inplace = True : ")
print(df)

