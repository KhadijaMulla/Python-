
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Salary(Employee):
    def calculate_salary(self):
        self.hra = self.basic_salary * 0.20
        self.da = self.basic_salary * 0.10
        self.gross_salary = self.basic_salary + self.hra + self.da


class Payslip(Salary):
    def display_payslip(self):
        self.calculate_salary()
        print("\nEmployee Salary Slip")
        self.display_employee()
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("Gross Salary:", self.gross_salary)


emp_id = input("Enter employee ID: ")
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

p = Payslip(emp_id, name, basic)
p.display_payslip()
