import os
import sys
from pymongo import MongoClient, errors

class Students:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        print("1. Roll no = ", self.roll_no)
        print("2. Name = ", self.name)
        print("3. Age = ", self.age)
        print("4. Marks =", self.marks)


class student_management:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
        self.db_name = os.getenv("MONGODB_DB", "student_management")
        self.client = None
        self.db = None
        self.students_collection = None
        self.connect_db()

    def connect_db(self):
        try:
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client[self.db_name]
            self.students_collection = self.db.students
            self.students_collection.create_index("roll_no", unique=True)
            print(f"Connected to MongoDB at {self.mongo_uri} (DB: {self.db_name})")
        except Exception as e:
            print("MongoDB connection failed:", e)
            sys.exit(1)

    def add_student(self):
        try:
            roll_no = int(input("Enter the roll no = "))
            name = input("Enter the Name = ")
            age = int(input("Enter the age = "))
            marks = int(input("Enter the marks = "))

            if not name:
                print("Name is required.")
                return

            student_doc = {
                "roll_no": roll_no,
                "name": name,
                "age": age,
                "marks": marks,
            }

            self.students_collection.insert_one(student_doc)
            print("Student created successfully.")
        except ValueError:
            print("Invalid input. Roll no, age, and marks must be numbers.")
        except errors.DuplicateKeyError:
            print(f"Student with roll no {roll_no} already exists.")
        except Exception as e:
            print("Error adding student:", e)

    def view_student(self):
        try:
            roll_no = int(input("Enter the roll no = "))
            student_doc = self.students_collection.find_one({"roll_no": roll_no})
            if student_doc is None:
                print("Student not found.")
                return

            student = Students(student_doc["roll_no"], student_doc["name"], student_doc["age"], student_doc["marks"])
            student.show_details()
        except ValueError:
            print("Invalid roll number.")
        except Exception as e:
            print("Error viewing student:", e)

    def update_studen(self):
        try:
            roll_no = int(input("Enter the roll no = "))
            student_doc = self.students_collection.find_one({"roll_no": roll_no})
            if student_doc is None:
                print("Student not found.")
                return

            name = input("Enter the new Name = ")
            age_input = input("Enter the new age = ")
            marks_input = input("Enter the new marks  = ")

            update_fields = {}
            if name:
                update_fields["name"] = name
            if age_input:
                update_fields["age"] = int(age_input)
            if marks_input:
                update_fields["marks"] = int(marks_input)

            if not update_fields:
                print("No changes provided.")
                return

            self.students_collection.update_one({"roll_no": roll_no}, {"$set": update_fields})
            print("Student updated successfully.")
        except ValueError:
            print("Invalid input.")
        except Exception as e:
            print("Error updating student:", e)

    def delete_student(self):
        try:
            roll_no = int(input("Enter the roll no = "))
            result = self.students_collection.delete_one({"roll_no": roll_no})
            if result.deleted_count == 0:
                print("Student not found.")
                return
            print(f"Student with roll no {roll_no} deleted.")
        except ValueError:
            print("Invalid roll number.")
        except Exception as e:
            print("An unexpected error occurred:", e)

student = student_management()

while True:
    print("============================Student Management System=====================")
    print("1. Add student : ")
    print("2. View Student : ")
    print("3. Update Student: ")
    print("4. Delete Student : ")
    print("5. Exit ")

    choice = input("Enter The option = ")
    if choice == "1":
        student.add_student()
    elif choice == "2":
        student.view_student()
    elif choice == "3":
        student.update_studen()
    elif choice == "4":
        student.delete_student()
    elif choice == "5":
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
