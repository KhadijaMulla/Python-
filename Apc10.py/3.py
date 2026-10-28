
import matplotlib.pyplot as plt

activities = ["Study", "Sleep", "Play", "Other"]
hours = [6, 8, 4, 6]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Time Distribution")
plt.legend()

plt.show()
