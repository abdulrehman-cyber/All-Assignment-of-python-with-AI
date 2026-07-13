"""
Student Management System - Core logic with file handling and advanced features
"""
import json
import os
from student import Students
from datetime import datetime


class StudentManagement:
    def __init__(self, filename="students_data.json"):
        self.students = {}
        self.filename = filename
        self.load_data()

    def save_data(self):
        """Save students data to JSON file"""
        try:
            data = {str(roll_no): student.to_dict() for roll_no, student in self.students.items()}
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            return True, "Data saved successfully!"
        except Exception as e:
            return False, f"Error saving data: {str(e)}"

    def load_data(self):
        """Load students data from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.students = {int(roll_no): Students.from_dict(student_data) 
                                   for roll_no, student_data in data.items()}
                return True, f"Loaded {len(self.students)} students from file"
            else:
                return True, "No data file found. Starting fresh!"
        except Exception as e:
            return False, f"Error loading data: {str(e)}"

    def add_student(self, roll_no, name, age, marks, email="", phone=""):
        """Add a new student"""
        try:
            if roll_no in self.students:
                return False, f"Student with roll number {roll_no} already exists!"
            
            if not (1 <= age <= 100):
                return False, "Age must be between 1 and 100!"
            
            if not (0 <= marks <= 100):
                return False, "Marks must be between 0 and 100!"
            
            student = Students(roll_no, name, age, marks, email, phone)
            self.students[roll_no] = student
            self.save_data()
            return True, f"Student {name} added successfully!"
        except ValueError:
            return False, "Invalid input data type!"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def view_student(self, roll_no):
        """View a specific student's details"""
        if roll_no in self.students:
            return True, self.students[roll_no].show_details()
        else:
            return False, "Student not found!"

    def update_student(self, roll_no, name=None, age=None, marks=None, email=None, phone=None):
        """Update student details"""
        try:
            if roll_no not in self.students:
                return False, "Student not found!"
            
            student = self.students[roll_no]
            
            if name:
                student.name = name
            if age:
                if not (1 <= age <= 100):
                    return False, "Age must be between 1 and 100!"
                student.age = age
            if marks is not None:
                if not (0 <= marks <= 100):
                    return False, "Marks must be between 0 and 100!"
                student.marks = marks
            if email:
                student.email = email
            if phone:
                student.phone = phone
            
            self.save_data()
            return True, "Student updated successfully!"
        except ValueError:
            return False, "Invalid input data type!"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def delete_student(self, roll_no):
        """Delete a student"""
        try:
            if roll_no not in self.students:
                return False, "Student not found!"
            
            name = self.students[roll_no].name
            del self.students[roll_no]
            self.save_data()
            return True, f"Student {name} deleted successfully!"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def get_all_students(self):
        """Get all students data"""
        return list(self.students.values())

    def search_students(self, query):
        """Search students by name or roll number"""
        results = []
        query_lower = str(query).lower()
        
        for student in self.students.values():
            if (query_lower in student.name.lower() or 
                query_lower == str(student.roll_no)):
                results.append(student)
        
        return results

    def get_statistics(self):
        """Get class statistics"""
        if not self.students:
            return None
        
        all_marks = [s.marks for s in self.students.values()]
        
        stats = {
            "total_students": len(self.students),
            "average_marks": round(sum(all_marks) / len(all_marks), 2),
            "highest_marks": max(all_marks),
            "lowest_marks": min(all_marks),
            "pass_count": sum(1 for s in self.students.values() if s.get_status() == "Pass"),
            "fail_count": sum(1 for s in self.students.values() if s.get_status() == "Fail"),
        }
        return stats

    def get_grade_distribution(self):
        """Get distribution of grades"""
        grades = {"A+": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for student in self.students.values():
            grade = student.get_grade()
            if grade in grades:
                grades[grade] += 1
        return grades

    def export_to_csv(self, filename="students_export.csv"):
        """Export students to CSV file"""
        try:
            import csv
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Roll No", "Name", "Age", "Marks", "Grade", "Status", "Email", "Phone"])
                for student in self.students.values():
                    details = student.show_details()
                    writer.writerow([
                        details["Roll No"],
                        details["Name"],
                        details["Age"],
                        details["Marks"],
                        details["Grade"],
                        details["Status"],
                        details["Email"],
                        details["Phone"]
                    ])
            return True, f"Data exported to {filename}"
        except Exception as e:
            return False, f"Error exporting: {str(e)}"

    def sort_by_marks(self, descending=True):
        """Sort students by marks"""
        return sorted(self.students.values(), 
                     key=lambda x: x.marks, 
                     reverse=descending)

    def sort_by_name(self):
        """Sort students by name"""
        return sorted(self.students.values(), 
                     key=lambda x: x.name)
