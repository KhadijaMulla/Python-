
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [25, 28, 30, 27, 32]

plt.plot(days, temperature, marker='o')

plt.title("Temperature Over Five Days")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()
