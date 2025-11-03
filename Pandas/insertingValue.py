import pandas as pd

data = {
    "Name":["Harshit", "Aus", "Ind", "Eng", "USA"],
    "Age" :[21,1000,1000000,100000,100000]
}

df = pd.DataFrame(data)

# Inserting columns in the data: 

df["Interests"] = ["Card Magic, Calisthenics, Chess" , "Catching Pythons", "Collecting Tax" , "Stealing" , "Saving the World (USA)"]



df.insert(0, "Total Money", [1200, 90000000, 100000000, 3000000, 40000000] )

print("Printing Updated dataset after adding 'Interests' and 'Total Money' column.")
print(df)

# Saving the Data:

# df.to_csv("D:\AI ML\randomData.csv")