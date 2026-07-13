# from tkinter import *

import tkinter as tk

window =tk.Tk()
window.title("student marksheet")
window.geometry("450 x 450")

frame = tk.Frame(window, padx=10, pady=10)
frame.pack()

result = tk.StringVar()
result.set("Result will appear here")

