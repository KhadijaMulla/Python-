
import numpy as np
import pandas as pd

marks = np.array([78, 85, 90, 67, 88])

series = pd.Series(marks, index=[
    "Student 1",
    "Student 2",
    "Student 3",
    "Student 4",
    "Student 5"
])

print("Student Marks:")
print(series)

print("\nAverage Marks:", series.mean())
print("Highest Marks:", series.max())
print("Lowest Marks:", series.min())
