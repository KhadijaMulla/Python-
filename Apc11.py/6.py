
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x350")

tk.Label(root, text="Simple Calculator",
         font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="First Number").pack()
num1 = tk.Entry(root)
num1.pack(pady=5)

tk.Label(root, text="Second Number").pack()
num2 = tk.Entry(root)
num2.pack(pady=5)

result = tk.Label(root, text="Result: ")
result.pack(pady=10)

def calculate(op):
    try:
        a = float(num1.get())
        b = float(num2.get())

        if op == "+":
            ans = a + b
        elif op == "-":
            ans = a - b
        elif op == "*":
            ans = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror(
                    "Error", "Cannot divide by zero"
                )
                return
            ans = a / b

        result.config(text="Result: " + str(ans))

    except ValueError:
        messagebox.showerror(
            "Error", "Enter valid numbers"
        )

tk.Button(root, text="Add",
          command=lambda: calculate("+")).pack(pady=3)
tk.Button(root, text="Subtract",
          command=lambda: calculate("-")).pack(pady=3)
tk.Button(root, text="Multiply",
          command=lambda: calculate("*")).pack(pady=3)
tk.Button(root, text="Divide",
          command=lambda: calculate("/")).pack(pady=3)

root.mainloop()
