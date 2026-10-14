project1 = {"A", "B", "C", "D"}
project2 = {"N", "K", "A", "S"}

print("Employees in both projects:", project1.intersection(project2))
print("Employees only in Project 1:", project1.difference(project2))
print("Employees only in Project 2:", project2.difference(project1))
print("All unique employees:", project1.union(project2))