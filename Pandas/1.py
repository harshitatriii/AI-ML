import pandas as pd

data = {
    "Names" : ["Harshit", "Aus", "Ind", "Eng", "USA"],
    "Age" : [21,2000,2000,500,1000]
}

# Creating the dataframe: 
df = pd.DataFrame(data)

print("Dataframe created is this: ")
print(df)

# selecting a particular column (series) :

dfNames = df[ ["Names"] ]

print("Printing Only Names: ")
print(dfNames)

# Filtering based on condintions: 

dfFiltered = df[df["Age"] < 100 ]

print("Printing Data Frame with age less than 100 :")
print(dfFiltered)

# Inserting columns in the data: 

df["Interests"] = ["Card Magic, Calisthenics, Chess" , "Catching Pythons", "Collecting Tax" , "Stealing" , "Saving the World (USA)"]



df.insert(0, "Total Money", [1200, 90000000, 100000000, 3000000, 40000000] )

print("Printing Updated dataset after adding 'Interests' and 'Total Money' column.")
print(df)