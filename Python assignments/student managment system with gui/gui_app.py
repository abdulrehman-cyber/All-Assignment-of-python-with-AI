"""
Student Management System - Modern GUI Application
Built with Tkinter for Windows
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from management import StudentManagement
import os


class StudentManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Color scheme
        self.bg_color = "#f0f0f0"
        self.primary_color = "#2c3e50"
        self.accent_color = "#3498db"
        self.success_color = "#27ae60"
        self.danger_color = "#e74c3c"
        
        self.root.configure(bg=self.bg_color)
        
        # Initialize management system
        self.management = StudentManagement()
        
        # Create GUI
        self.create_widgets()
        self.refresh_table()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Header Frame
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=60)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title_label = tk.Label(
            header_frame,
            text="📚 Student Management System",
            font=("Arial", 20, "bold"),
            bg=self.primary_color,
            fg="white"
        )
        title_label.pack(pady=10)
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left Panel - Input Form
        self.create_input_form(content_frame)
        
        # Right Panel - Display Table
        self.create_table_frame(content_frame)
        
        # Bottom Panel - Buttons
        self.create_button_panel()
    
    def create_input_form(self, parent):
        """Create input form for student details"""
        form_frame = tk.LabelFrame(
            parent,
            text="Add/Update Student",
            font=("Arial", 12, "bold"),
            bg="white",
            padx=15,
            pady=15
        )
        form_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10), pady=5)
        
        # Roll Number
        tk.Label(form_frame, text="Roll No:", bg="white", font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.roll_no_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
        self.roll_no_entry.grid(row=0, column=1, pady=5, sticky=tk.EW)
        
        # Name
        tk.Label(form_frame, text="Name:", bg="white", font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
        self.name_entry.grid(row=1, column=1, pady=5, sticky=tk.EW)
        
        # Age
        tk.Label(form_frame, text="Age:", bg="white", font=("Arial", 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.age_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
        self.age_entry.grid(row=2, column=1, pady=5, sticky=tk.EW)
        
        # Marks
        tk.Label(form_frame, text="Marks (0-100):", bg="white", font=("Arial", 10)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.marks_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
        self.marks_entry.grid(row=3, column=1, pady=5, sticky=tk.EW)
        
        # Email
        tk.Label(form_frame, text="Email:", bg="white", font=("Arial", 10)).grid(row=4, column=0, sticky=tk.W, pady=5)
        self.email_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
        self.email_entry.grid(row=4, column=1, pady=5, sticky=tk.EW)
        
        # Phone
        tk.Label(form_frame, text="Phone:", bg="white", font=("Arial", 10)).grid(row=5, column=0, sticky=tk.W, pady=5)
        self.phone_entry = tk.Entry(form_frame, width=25, font=("Arial", 10))
        self.phone_entry.grid(row=5, column=1, pady=5, sticky=tk.EW)
        
        # Buttons Frame
        buttons_frame = tk.Frame(form_frame, bg="white")
        buttons_frame.grid(row=6, column=0, columnspan=2, pady=15, sticky=tk.EW)
        
        add_btn = tk.Button(
            buttons_frame,
            text="➕ Add Student",
            bg=self.accent_color,
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.add_student,
            width=12
        )
        add_btn.pack(side=tk.LEFT, padx=5)
        
        update_btn = tk.Button(
            buttons_frame,
            text="✏️ Update",
            bg=self.success_color,
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.update_student,
            width=12
        )
        update_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            buttons_frame,
            text="🔄 Clear",
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.clear_form,
            width=12
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Search Frame
        search_frame = tk.LabelFrame(
            form_frame,
            text="Search",
            font=("Arial", 11, "bold"),
            bg="white",
            padx=10,
            pady=10
        )
        search_frame.grid(row=7, column=0, columnspan=2, pady=15, sticky=tk.EW)
        
        tk.Label(search_frame, text="Search by Name/Roll:", bg="white", font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame, width=20, font=("Arial", 9))
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<KeyRelease>', lambda e: self.search_student())
        
        # Statistics Frame
        stats_frame = tk.LabelFrame(
            form_frame,
            text="Statistics",
            font=("Arial", 11, "bold"),
            bg="white",
            padx=10,
            pady=10
        )
        stats_frame.grid(row=8, column=0, columnspan=2, pady=10, sticky=tk.EW)
        
        stats_btn = tk.Button(
            stats_frame,
            text="📊 View Statistics",
            bg="#9b59b6",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.show_statistics,
            width=25
        )
        stats_btn.pack(pady=5)
        
        export_btn = tk.Button(
            stats_frame,
            text="📥 Export to CSV",
            bg="#e67e22",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.export_csv,
            width=25
        )
        export_btn.pack(pady=5)
        
        form_frame.columnconfigure(1, weight=1)
    
    def create_table_frame(self, parent):
        """Create table to display students"""
        table_frame = tk.LabelFrame(
            parent,
            text="Student Records",
            font=("Arial", 12, "bold"),
            bg="white",
            padx=10,
            pady=10
        )
        table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=5)
        
        # Create Treeview
        columns = ("Roll No", "Name", "Age", "Marks", "Grade", "Status", "Email")
        self.tree = ttk.Treeview(table_frame, columns=columns, height=20, show="headings")
        
        # Define column headings and widths
        column_widths = {
            "Roll No": 60,
            "Name": 100,
            "Age": 40,
            "Marks": 60,
            "Grade": 60,
            "Status": 60,
            "Email": 150
        }
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col])
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        
        # Grid layout
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        vsb.grid(row=0, column=1, sticky=tk.NS)
        hsb.grid(row=1, column=0, sticky=tk.EW)
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Bind double-click to load student data
        self.tree.bind("<Double-1>", self.load_student_data)
        
        # Right-click menu
        self.tree.bind("<Button-3>", self.show_context_menu)
    
    def create_button_panel(self):
        """Create bottom button panel"""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        delete_btn = tk.Button(
            button_frame,
            text="🗑️ Delete Selected",
            bg=self.danger_color,
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.delete_student,
            width=18
        )
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        refresh_btn = tk.Button(
            button_frame,
            text="🔄 Refresh",
            bg="#34495e",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.refresh_table,
            width=18
        )
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        exit_btn = tk.Button(
            button_frame,
            text="❌ Exit",
            bg="#c0392b",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.root.quit,
            width=18
        )
        exit_btn.pack(side=tk.LEFT, padx=5)
    
    def add_student(self):
        """Add a new student"""
        try:
            roll_no = int(self.roll_no_entry.get())
            name = self.name_entry.get().strip()
            age = int(self.age_entry.get())
            marks = int(self.marks_entry.get())
            email = self.email_entry.get().strip()
            phone = self.phone_entry.get().strip()
            
            if not name:
                messagebox.showerror("Error", "Name cannot be empty!")
                return
            
            success, message = self.management.add_student(roll_no, name, age, marks, email, phone)
            
            if success:
                messagebox.showinfo("Success", message)
                self.clear_form()
                self.refresh_table()
            else:
                messagebox.showerror("Error", message)
        
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data types!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def update_student(self):
        """Update selected student"""
        try:
            roll_no = int(self.roll_no_entry.get())
            name = self.name_entry.get().strip()
            age_str = self.age_entry.get().strip()
            marks_str = self.marks_entry.get().strip()
            email = self.email_entry.get().strip()
            phone = self.phone_entry.get().strip()
            
            age = int(age_str) if age_str else None
            marks = int(marks_str) if marks_str else None
            
            success, message = self.management.update_student(
                roll_no, name if name else None, age, marks, 
                email if email else None, phone if phone else None
            )
            
            if success:
                messagebox.showinfo("Success", message)
                self.clear_form()
                self.refresh_table()
            else:
                messagebox.showerror("Error", message)
        
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def delete_student(self):
        """Delete selected student"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to delete!")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            try:
                item = self.tree.item(selected[0])
                roll_no = int(item['values'][0])
                
                success, message = self.management.delete_student(roll_no)
                
                if success:
                    messagebox.showinfo("Success", message)
                    self.refresh_table()
                else:
                    messagebox.showerror("Error", message)
            
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def load_student_data(self, event):
        """Load student data into form when double-clicked"""
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            values = item['values']
            
            self.clear_form()
            self.roll_no_entry.insert(0, values[0])
            self.name_entry.insert(0, values[1])
            self.age_entry.insert(0, values[2])
            self.marks_entry.insert(0, values[3])
            
            # Get full student data including email and phone
            try:
                success, student_data = self.management.view_student(int(values[0]))
                if success:
                    self.email_entry.insert(0, student_data.get("Email", ""))
                    self.phone_entry.insert(0, student_data.get("Phone", ""))
            except:
                pass
    
    def clear_form(self):
        """Clear all input fields"""
        self.roll_no_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
    
    def refresh_table(self):
        """Refresh the student table"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add all students
        students = self.management.get_all_students()
        for student in students:
            details = student.show_details()
            self.tree.insert(
                "",
                tk.END,
                values=(
                    details["Roll No"],
                    details["Name"],
                    details["Age"],
                    details["Marks"],
                    details["Grade"],
                    details["Status"],
                    details["Email"]
                )
            )
    
    def search_student(self):
        """Search students"""
        query = self.search_entry.get().strip()
        
        # Clear table
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if query:
            results = self.management.search_students(query)
            for student in results:
                details = student.show_details()
                self.tree.insert(
                    "",
                    tk.END,
                    values=(
                        details["Roll No"],
                        details["Name"],
                        details["Age"],
                        details["Marks"],
                        details["Grade"],
                        details["Status"],
                        details["Email"]
                    )
                )
        else:
            self.refresh_table()
    
    def show_statistics(self):
        """Show class statistics"""
        stats = self.management.get_statistics()
        
        if not stats:
            messagebox.showinfo("Statistics", "No students in the system!")
            return
        
        grades = self.management.get_grade_distribution()
        
        message = f"""
📊 CLASS STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Students: {stats['total_students']}
Average Marks: {stats['average_marks']}
Highest Marks: {stats['highest_marks']}
Lowest Marks: {stats['lowest_marks']}
Pass Count: {stats['pass_count']}
Fail Count: {stats['fail_count']}

📈 GRADE DISTRIBUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━
A+: {grades['A+']}
A:  {grades['A']}
B:  {grades['B']}
C:  {grades['C']}
D:  {grades['D']}
F:  {grades['F']}
        """
        
        messagebox.showinfo("Statistics", message)
    
    def export_csv(self):
        """Export data to CSV"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filename:
            success, message = self.management.export_to_csv(filename)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
    
    def show_context_menu(self, event):
        """Show right-click context menu"""
        item = self.tree.selection()
        if item:
            menu = tk.Menu(self.root, tearoff=0)
            menu.add_command(label="View Details", command=lambda: self.view_details())
            menu.add_command(label="Edit", command=lambda: self.load_student_data(event))
            menu.add_separator()
            menu.add_command(label="Delete", command=self.delete_student)
            
            menu.tk_popup(event.x_root, event.y_root)
    
    def view_details(self):
        """View full details of selected student"""
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            roll_no = int(item['values'][0])
            
            success, student_data = self.management.view_student(roll_no)
            
            if success:
                message = f"""
📋 STUDENT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Roll Number: {student_data['Roll No']}
Name: {student_data['Name']}
Age: {student_data['Age']}
Marks: {student_data['Marks']}
Grade: {student_data['Grade']}
Status: {student_data['Status']}
Email: {student_data['Email']}
Phone: {student_data['Phone']}
                """
                messagebox.showinfo("Student Details", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementGUI(root)
    root.mainloop()
