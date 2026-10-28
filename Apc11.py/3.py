
import tkinter as tk

root = tk.Tk()
root.title("Pack Layout Example")
root.geometry("350x300")

tk.Label(root, text="Pack Layout Manager",
         font=("Arial", 16)).pack(pady=15)

tk.Button(root, text="Home").pack(
    fill="x", padx=40, pady=5
)
tk.Button(root, text="About").pack(
    fill="x", padx=40, pady=5
)
tk.Button(root, text="Contact").pack(
    fill="x", padx=40, pady=5
)

root.mainloop()
