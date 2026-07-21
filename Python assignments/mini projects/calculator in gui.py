# import random
# def random_guessing_number():
#     print("WELCOME TO GUESSING NUMBER GAME")
#     print("I am thinking ")
    
    
    
    
#     secrat_number=random.randiant(1,10)
import tkinter as tk

# ---------------- Functions ---------------- #

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
# root.resizable(False, False)

# ---------------- Entry ---------------- #

entry = tk.Entry(
    root,
    font=("Arial", 20),
    justify="right",
    bd=8
)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ---------------- Buttons ---------------- #

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            command=calculate
        )
    else:
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda value=text: click(value)
        )

    btn.grid(row=row, column=col, padx=5, pady=5)

# ---------------- Clear Button ---------------- #

clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    width=24,
    height=2,
    command=clear
)

clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
button = tk.Button(
    root,
    text="Submit",
    command="submit"
)
button.pack(pady=10)

root.mainloop()