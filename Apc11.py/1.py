
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")

label = tk.Label(
    root,
    text="Welcome to Python GUI",
    font=("Arial", 16)
)
label.pack(pady=50)

root.mainloop()
