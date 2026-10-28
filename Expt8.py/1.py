
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, course, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display_student(self):
        self.display_person()
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.marks)


name = input("Enter student name: ")
age = int(input("Enter age: "))
roll_no = input("Enter roll number: ")
course = input("Enter course: ")
marks = float(input("Enter marks: "))

s = Student(name, age, roll_no, course, marks)

print("\nStudent Information")
s.display_student()
