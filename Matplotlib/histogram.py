import matplotlib.pyplot as plt

ages = [1,1,1,1,2,3,3,4,5,5,5,8,9,13,15,16,19,20,21,21,22,23,21,23,60,49,50,70,100,99,98,96,97,100,100,101]

plt.hist(ages, bins=5, label="Indian People Age  Distribution", color="coral" , edgecolor = "black")

plt.legend()
plt.xlabel("Age")
plt.ylabel("No. Of People")
plt.show()