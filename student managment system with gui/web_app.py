"""
Student Management System - Full Stack Web Application
Flask Backend with SQLAlchemy Database
"""

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)


# Database Model
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    marks = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(120), default="")
    phone = db.Column(db.String(20), default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
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
    
    def to_dict(self):
        """Convert student to dictionary"""
        return {
            "id": self.id,
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "marks": self.marks,
            "email": self.email,
            "phone": self.phone,
            "grade": self.get_grade(),
            "status": self.get_status(),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }


# Create tables
with app.app_context():
    db.create_all()


# Routes

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/api/students', methods=['GET'])
def get_students():
    """Get all students"""
    try:
        students = Student.query.all()
        return jsonify({
            "success": True,
            "count": len(students),
            "data": [student.to_dict() for student in students]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get specific student"""
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({"success": False, "error": "Student not found"}), 404
        
        return jsonify({"success": True, "data": student.to_dict()})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/students', methods=['POST'])
def add_student():
    """Add new student"""
    try:
        data = request.get_json()
        
        # Validation
        if not data.get('roll_no') or not data.get('name'):
            return jsonify({"success": False, "error": "Roll No and Name are required"}), 400
        
        if Student.query.filter_by(roll_no=data['roll_no']).first():
            return jsonify({"success": False, "error": f"Roll No {data['roll_no']} already exists"}), 400
        
        age = int(data.get('age', 0))
        marks = float(data.get('marks', 0))
        
        if not (1 <= age <= 100):
            return jsonify({"success": False, "error": "Age must be between 1 and 100"}), 400
        
        if not (0 <= marks <= 100):
            return jsonify({"success": False, "error": "Marks must be between 0 and 100"}), 400
        
        student = Student(
            roll_no=int(data['roll_no']),
            name=data['name'],
            age=age,
            marks=marks,
            email=data.get('email', ''),
            phone=data.get('phone', '')
        )
        
        db.session.add(student)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": f"Student {student.name} added successfully!",
            "data": student.to_dict()
        }), 201
    
    except ValueError as e:
        return jsonify({"success": False, "error": "Invalid input data type"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update student"""
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({"success": False, "error": "Student not found"}), 404
        
        data = request.get_json()
        
        if 'name' in data:
            student.name = data['name']
        if 'age' in data:
            age = int(data['age'])
            if not (1 <= age <= 100):
                return jsonify({"success": False, "error": "Age must be between 1 and 100"}), 400
            student.age = age
        if 'marks' in data:
            marks = float(data['marks'])
            if not (0 <= marks <= 100):
                return jsonify({"success": False, "error": "Marks must be between 0 and 100"}), 400
            student.marks = marks
        if 'email' in data:
            student.email = data['email']
        if 'phone' in data:
            student.phone = data['phone']
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Student updated successfully!",
            "data": student.to_dict()
        })
    
    except ValueError:
        return jsonify({"success": False, "error": "Invalid input data type"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete student"""
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({"success": False, "error": "Student not found"}), 404
        
        name = student.name
        db.session.delete(student)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": f"Student {name} deleted successfully!"
        })
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/search', methods=['GET'])
def search_students():
    """Search students by name or roll number"""
    try:
        query = request.args.get('q', '').lower()
        
        if not query:
            return jsonify({"success": False, "error": "Search query required"}), 400
        
        students = Student.query.filter(
            (Student.name.ilike(f'%{query}%')) | 
            (Student.roll_no == int(query) if query.isdigit() else False)
        ).all()
        
        return jsonify({
            "success": True,
            "count": len(students),
            "data": [student.to_dict() for student in students]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics"""
    try:
        total_students = Student.query.count()
        avg_marks = db.session.query(db.func.avg(Student.marks)).scalar() or 0
        passed = Student.query.filter(Student.marks >= 40).count()
        failed = Student.query.filter(Student.marks < 40).count()
        
        return jsonify({
            "success": True,
            "data": {
                "total_students": total_students,
                "avg_marks": round(float(avg_marks), 2),
                "passed": passed,
                "failed": failed
            }
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    print("🚀 Starting Student Management System Web App...")
    print("📍 Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
