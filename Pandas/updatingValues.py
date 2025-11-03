import pandas as pd

data = {
    "Names" : ["Harshit", "Aus", "Ind", "Eng", "USA"],
    "Age" : [21,2000,2000,500,1000]
}

df = pd.DataFrame(data)

print("DataFrame: " )


# updating: 

df["Age"] = 1000
print(df)

df["Paisa"] = [150,1000,2000,100,3000]

# Updating a single value: 
df.loc[0, "Age"] = 21

print("Updated row 0, 'Age' column value to 21 : " )
print(df)

# Updating Multiple Values Altogether :
print("Updating Paisa Column by 10 % : ") 
df["Paisa"] = df["Paisa"] * 1.10

print(df)

# df.loc()