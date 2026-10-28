
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Form")
root.geometry("350x200")

tk.Label(root, text="Username:").grid(
    row=0, column=0, padx=10, pady=10
)
username = tk.Entry(root)
username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(
    row=1, column=0, padx=10, pady=10
)
password = tk.Entry(root, show="*")
password.grid(row=1, column=1, padx=10, pady=10)

def login():
    if username.get() and password.get():
        messagebox.showinfo("Login", "Login submitted")
    else:
        messagebox.showwarning(
            "Login", "Enter username and password"
        )

tk.Button(root, text="Login",
          command=login).grid(
              row=2, column=1, pady=10
          )

root.mainloop()
