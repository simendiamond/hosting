import tkinter as tk
from tkinter import ttk
root = tk.Tk()
f = "lamp"
root.geometry("50x200")
root.title(f)
button1 = ttk.Button(root, text="click")
button1.pack(side="left")
b = ttk.Checkbutton(root, text="male")
b.pack(side="right")
b2 = ttk.Checkbutton(root, text="female")
b2.pack(side="right")
gh = ttk.Radiobutton(root, text="female")
gh.pack(side="bottom")
root.mainloop()