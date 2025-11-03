import matplotlib.pyplot as plt

year = [2015,2016,2021,2025]
centuries = [7,16,1,3]

plt.plot(year,centuries, color ="orange", linestyle = "--" , marker = "o", label = "Virat Kohli's Centuries Info" )
plt.legend()
plt.xlabel("Year")
plt.ylabel("Centuries")
plt.title("Kohli's Yearly Centuries Report")
plt.grid()
plt.show()



print("Success")

