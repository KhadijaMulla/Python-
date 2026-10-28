
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")

tk.Label(root, text="Registration Form",
         font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

gender = tk.StringVar(value="Male")

tk.Label(root, text="Select Gender:").pack()
tk.Radiobutton(root, text="Male",
               variable=gender, value="Male").pack()
tk.Radiobutton(root, text="Female",
               variable=gender, value="Female").pack()

agree = tk.IntVar()
tk.Checkbutton(root, text="I confirm my details",
               variable=agree).pack(pady=10)

def submit():
    name = name_entry.get()
    if name:
        messagebox.showinfo(
            "Welcome",
            f"Hello {name}! Gender: {gender.get()}"
        )
    else:
        messagebox.showwarning(
            "Warning", "Please enter your name"
        )

tk.Button(root, text="Submit",
          command=submit).pack(pady=10)

root.mainloop()
