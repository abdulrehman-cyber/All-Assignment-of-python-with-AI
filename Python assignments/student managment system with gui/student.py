"""
Student Class - Represents individual student data
"""

class Students:
    def __init__(self, roll_no, name, age, marks, email="", phone=""):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks
        self.email = email
        self.phone = phone

    def get_grade(self):
        """Calculate grade based on marks"""
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def get_status(self):
        """Check if student passed or failed"""
        return "Pass" if self.marks >= 40 else "Fail"

    def show_details(self):
        """Display student details"""
        return {
            "Roll No": self.roll_no,
            "Name": self.name,
            "Age": self.age,
            "Marks": self.marks,
            "Grade": self.get_grade(),
            "Status": self.get_status(),
            "Email": self.email,
            "Phone": self.phone
        }

    def to_dict(self):
        """Convert student to dictionary for JSON storage"""
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "marks": self.marks,
            "email": self.email,
            "phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        """Create student object from dictionary"""
        return Students(
            data["roll_no"],
            data["name"],
            data["age"],
            data["marks"],
            data.get("email", ""),
            data.get("phone", "")
        )
