class Calculator:

    def add(self, a, b, c=0, d=0):
        return a + b + c + d


calc = Calculator()

print("Addition of 2 numbers:", calc.add(10, 20))
print("Addition of 3 numbers:", calc.add(10, 20, 30))
print("Addition of 4 numbers:", calc.add(10, 20, 30, 40))