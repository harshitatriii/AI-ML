import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,18,6,20]

plt.subplot(1,2,1)
plt.plot(x,y , label = "Plot char")
plt.title("Travelling Line Chart")
plt.xlabel("No.of wheels")
plt.ylabel("People Travelling")
plt.legend()

plt.subplot(1,2,2)
plt.bar(x,y, label="Bar Chart")
plt.title("Travelling Bar Chart")
plt.xlabel("No.of wheels")
plt.ylabel("People Travelling")
plt.legend()


plt.tight_layout()
plt.show()