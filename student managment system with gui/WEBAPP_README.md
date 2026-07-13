# 🎓 Student Management System - Web App

A modern full-stack web application for managing student records with a Flask backend and interactive frontend.

## ✨ Features

- ✅ **Add Students** - Add new student records with roll number, name, age, marks, email, and phone
- ✅ **View Students** - View all students in a clean, organized table
- ✅ **Edit Students** - Update student information easily
- ✅ **Delete Students** - Remove student records
- ✅ **Automatic Grade Calculation** - Grades are calculated automatically based on marks:
  - A+ (90+), A (80-89), B (70-79), C (60-69), D (50-59), F (<50)
- ✅ **Pass/Fail Status** - Automatic status calculation (Pass: ≥40, Fail: <40)
- ✅ **Search Functionality** - Search students by name or roll number
- ✅ **Statistics Dashboard** - View system statistics (total students, average marks, pass/fail count)
- ✅ **Data Persistence** - All data is stored in SQLite database
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **Modern UI** - Bootstrap 5 with custom styling

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python web_app.py
   ```

3. **Access the Application**
   - Open your web browser and go to: **http://localhost:5000**

## 📁 Project Structure

```
.
├── web_app.py                 # Main Flask application
├── requirements.txt           # Python dependencies
├── students.db               # SQLite database (created automatically)
├── templates/
│   └── index.html            # Frontend HTML template
└── static/
    ├── css/
    │   └── style.css         # Custom styling
    └── js/
        └── script.js         # Frontend JavaScript
```

## 🔌 API Endpoints

### Get All Students
```
GET /api/students
```

### Get Specific Student
```
GET /api/students/<student_id>
```

### Add New Student
```
POST /api/students
Content-Type: application/json

{
    "roll_no": 101,
    "name": "Ahmed Khan",
    "age": 20,
    "marks": 85.5,
    "email": "ahmed@example.com",
    "phone": "+92-3001234567"
}
```

### Update Student
```
PUT /api/students/<student_id>
Content-Type: application/json

{
    "name": "Updated Name",
    "age": 21,
    "marks": 90,
    "email": "newemail@example.com",
    "phone": "+92-3009876543"
}
```

### Delete Student
```
DELETE /api/students/<student_id>
```

### Search Students
```
GET /api/search?q=name_or_rollno
```

### Get Statistics
```
GET /api/stats
```

## 📊 Database Schema

### Students Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary Key |
| roll_no | Integer | Unique roll number |
| name | String | Student name |
| age | Integer | Student age |
| marks | Float | Student marks (0-100) |
| email | String | Email address |
| phone | String | Phone number |
| created_at | DateTime | Record creation timestamp |

## 🎨 UI Features

### Sidebar
- **Add Student Form** - Quick add new students
- **Search Bar** - Search functionality with clear button

### Main Area
- **Students Table** - Displays all student records with actions
- **Alert Messages** - Success, error, warning, and info notifications
- **Edit Modal** - Pop-up form for editing student details
- **Stats Modal** - Dashboard showing system statistics

## 🔒 Validation Rules

- **Roll Number** - Required, must be unique
- **Name** - Required, text field
- **Age** - Required, must be between 1-100
- **Marks** - Required, must be between 0-100
- **Email** - Optional, must be valid email format
- **Phone** - Optional, text field

## 🎯 Grade System

| Grade | Marks | Color |
|-------|-------|-------|
| A+ | 90+ | Green |
| A | 80-89 | Green |
| B | 70-79 | Cyan |
| C | 60-69 | Yellow |
| D | 50-59 | Orange |
| F | <50 | Red |

## 📱 Responsive Design

The application is fully responsive and works on:
- ✅ Desktop computers
- ✅ Tablets
- ✅ Mobile phones

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome 6

## 🚨 Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify the last line in `web_app.py`:
```python
app.run(debug=True, port=5001)  # Change port number
```

### Database Errors
Delete `students.db` and restart the application to create a fresh database.

### Dependencies Issues
```bash
pip install --upgrade -r requirements.txt
```

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created for Student Management System - Web Version

---

**Enjoy managing your student records! 🎓**
