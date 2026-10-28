
import matplotlib.pyplot as plt

marks = [45, 56, 67, 72, 85, 90, 62, 74,
         81, 55, 68, 92, 77, 49, 88]

plt.hist(marks, bins=5, edgecolor='black')

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
