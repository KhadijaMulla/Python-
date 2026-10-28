
import pandas as pd

data = {
    "Roll No": [101, 102, 103, 104],
    "Name": ["Ayesha", "Rahul", "Priya", "Aman"],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Student Records:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Students Scoring Above 80:")
print(df[df["Marks"] > 80])
