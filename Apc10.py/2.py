
import matplotlib.pyplot as plt

students = ["Ayesha", "Rahul", "Priya", "Aman", "Sara"]
marks = [85, 78, 92, 88, 75]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
