import tkinter as tk
from tkinter import messagebox



window =tk.Tk()
window.title("student marksheet")
window.geometry("450x450")

frame = tk.Frame(window, padx=10, pady=10)
frame.pack()

result = tk.StringVar()
result.set("Result will appear here")


tk.Label(frame, text="Student Name:").grid(row=0, column=0, sticky="w")
tk.Label(frame, text="English (Out of 100): ").grid(row=1, column=0, sticky="w")
tk.Label(frame, text="Maths (Out of 100): ").grid(row=2, column=0, sticky="w")
tk.Label(frame, text="Urdu (Out of 100): ").grid(row=3, column=0, sticky="w")


name_entry = tk.Entry(frame)
english_entry = tk.Entry(frame)
maths_entry = tk.Entry(frame)
urdu_entry = tk.Entry(frame)

name_entry.grid(row=0, column=1)
english_entry.grid(row=1, column=1)
maths_entry.grid(row=2, column=1)
urdu_entry.grid(row=3, column=1)




def generate_result():
    
    name = name_entry.get()
    try:
        english_marks = int(english_entry.get())
        maths_marks = int(maths_entry.get())
        urdu_marks = int(urdu_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric marks for all subjects.")
        return
    
    
    total = 300
    obtained = english_marks + maths_marks + urdu_marks
    percentage = (obtained / total) * 100
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    result.set(f"Name: {name}\n"
               f"Total Marks: {total}\n"
               f"Obtained Marks: {obtained}\n"
               f"Percentage: {percentage:.2f}%\n"
               f"Grade: {grade}")

def clear():
    name_entry.delete(0, tk.END)
    english_entry.delete(0, tk.END)
    maths_entry.delete(0, tk.END)
    urdu_entry.delete(0, tk.END)
    result.set("Result cleared")


def sample():
    name_entry.delete(0, tk.END)
    name_entry.insert(0, "Abdul Rehman")
    
    english_entry.delete(0, tk.END)
    english_entry.insert(0, "67")
    
    maths_entry.delete(0, tk.END)
    maths_entry.insert(0, "86")
    
    urdu_entry.delete(0, tk.END)
    urdu_entry.insert(0, "95")
    
    


tk.Button(frame, text="Generate Result",
          command=generate_result).grid(row=4, 
                                        column=0, 
                                        pady=10)

tk.Button(frame,
          text="Clear",
          command=clear).grid(row=4,
                              column=1)

tk.Button(frame,
          text="Sample",
          command=sample).grid(row=5,
                               column= 0,
                               columnspan=2)


tk.Label(frame, 
         textvariable=result,
         fg="blue").grid(row=6, column=0, columnspan=2, pady=15)

window.mainloop()