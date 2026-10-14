# Input
age = int(input("Enter your current age: "))
height = float(input("Enter your current height: "))
name = input("Enter your name: ")

is_student = input("Are you a student? (True/False): ")
is_student = is_student.lower() == "True"

print("\n User Details ")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

next_year_age = age + 1 
name_upper = name.upper()

print("\n Processed Data ")
print("Age next year:", next_year_age)
print("Name in uppercase:", name_upper)

if is_student:
    print(name, "is a School student.")
else:
    print(name, "is a Collage student.")