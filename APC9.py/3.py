
import numpy as np

marks = np.array([
    [80, 75, 90],
    [85, 88, 78],
    [92, 80, 85]
])

print("Marks Array:")
print(marks)

print("Total Marks of Students:")
print(np.sum(marks, axis=1))

print("Average Marks in Each Subject:")
print(np.mean(marks, axis=0))
