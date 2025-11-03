import matplotlib.pyplot as plt

countries = ["India", "Afg", "Srilanka", "Bhutan"]

landArea = [1000 , 100 , 40, 30]

plt.pie(landArea, labels = countries , autopct="%1.1f%%")
plt.title("Land Area of Countries")

plt.show()