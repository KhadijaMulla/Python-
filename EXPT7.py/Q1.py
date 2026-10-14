class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

        # Calling parent class method
        self.display_person_info()


# Creating an Employee object
employee = Employee("Khadija", 21, "EMP101", 50000)

# Display employee details
employee.display_employee_info()