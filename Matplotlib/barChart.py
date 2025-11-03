import matplotlib.pyplot as plt

year = [2022,2023,2024,2025,2026]
tomatoes = [6000, 10000, 12000, 11000,7000]

plt.bar(year, tomatoes , color="seagreen",label = "Tomatoes eaten in KG" )


plt.xlabel("Year")
plt.ylabel("tomatoes in KGs")
plt.title("Tomatoes eaten per year")
plt.grid()
plt.legend()



plt.show()
