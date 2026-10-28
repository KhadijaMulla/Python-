
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Place Layout Example")
root.geometry("400x250")

tk.Label(root, text="Enter Your Name:",
         font=("Arial", 12)).place(x=30, y=40)

name_entry = tk.Entry(root)
name_entry.place(x=170, y=40)

def greet():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Greeting", "Hello " + name)
    else:
        messagebox.showwarning(
            "Warning", "Please enter your name"
        )

tk.Button(root, text="Greet",
          command=greet).place(x=170, y=100)

root.mainloop()
