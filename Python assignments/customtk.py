import customtkinter as ctk

ctk.set_appearance_mode("black")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("My App")
window.geometry("500x400")

window.mainloop()