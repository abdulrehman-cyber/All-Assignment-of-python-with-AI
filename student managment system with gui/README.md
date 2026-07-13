# 📚 Student Management System

A modern, feature-rich Student Management System with GUI, built using Python and Tkinter.

## Features

### ✨ Core Features
- **Add Students**: Add new students with roll number, name, age, marks, email, and phone
- **View Students**: Display all students in a sorted table
- **Update Students**: Modify any student's information
- **Delete Students**: Remove students from the system
- **Search**: Search students by name or roll number in real-time

### 🔧 Advanced Features
- **Grade Calculation**: Automatic grade assignment (A+, A, B, C, D, F) based on marks
- **Pass/Fail Status**: Automatic status determination
- **Statistics Dashboard**: 
  - Total students count
  - Average marks
  - Highest and lowest marks
  - Pass/Fail statistics
  - Grade distribution chart
- **Data Sorting**: Sort students by marks or name
- **Export to CSV**: Export all data to CSV file for further analysis

### 💾 File Handling
- **Persistent Storage**: All data is automatically saved to `students_data.json`
- **Auto-load**: Data is loaded automatically when the application starts
- **JSON Format**: Easy to backup, transfer, and integrate with other systems

### 🎨 Modern GUI
- **Professional Interface**: Clean and intuitive Tkinter GUI
- **Responsive Design**: Works on different screen sizes
- **Color-coded**: Easy-to-read interface with meaningful colors
- **Double-click to Edit**: Double-click any student to load their data for editing
- **Right-click Context Menu**: Quick access to view, edit, or delete options

## System Requirements
- Python 3.7 or higher
- Tkinter (usually comes with Python)
- CSV module (built-in)
- JSON module (built-in)

## Installation

1. Ensure Python is installed on your system
2. All required modules are built-in with Python, so no additional installation needed

## File Structure

```
New folder/
├── gui_app.py              # Main GUI application (RUN THIS FILE)
├── student.py              # Student class definition
├── management.py           # Student management logic with file handling
├── students_data.json      # Data file (created automatically)
└── students_export.csv     # Exported data (created on export)
```

## How to Use

### Starting the Application
```bash
cd "New folder"
python gui_app.py
```

### Adding a Student
1. Fill in all the fields in the left panel
2. Click the "➕ Add Student" button
3. Data will be saved automatically

### Viewing Students
- All students are displayed in the table on the right
- Use the search box to find students by name or roll number

### Editing a Student
**Method 1: Double-click**
1. Double-click any student in the table
2. Their data will load into the form
3. Modify the fields
4. Click "✏️ Update" button

**Method 2: Right-click menu**
1. Right-click on a student
2. Select "Edit" from the menu

### Deleting a Student
1. Click on a student in the table to select them
2. Click the "🗑️ Delete Selected" button or right-click and select "Delete"
3. Confirm the deletion

### Searching Students
- Type in the "Search by Name/Roll" box
- Results will filter in real-time
- Leave empty to see all students

### Viewing Statistics
- Click the "📊 View Statistics" button
- View total students, average marks, grades, and more

### Exporting Data
- Click "📥 Export to CSV" button
- Choose a location to save the CSV file
- Open with Excel or any spreadsheet application

## Data Format

### JSON Format (students_data.json)
```json
{
    "1": {
        "roll_no": 1,
        "name": "Ahmed Ali",
        "age": 20,
        "marks": 85,
        "email": "ahmed@example.com",
        "phone": "03001234567"
    }
}
```

### CSV Export Format
```
Roll No,Name,Age,Marks,Grade,Status,Email,Phone
1,Ahmed Ali,20,85,A,Pass,ahmed@example.com,03001234567
```

## Grade Scale
- **A+**: 90-100
- **A**: 80-89
- **B**: 70-79
- **C**: 60-69
- **D**: 50-59
- **F**: Below 50

Pass: Marks ≥ 40
Fail: Marks < 40

## Keyboard Shortcuts
- Double-click: Load student data for editing
- Right-click: Context menu options

## Troubleshooting

### Application won't start
- Check if Python is installed: `python --version`
- Ensure all files are in the same directory

### Data not saving
- Check if `students_data.json` file is writable
- Ensure the folder has write permissions

### Export not working
- Choose a valid location for saving
- Ensure the drive has sufficient space

## Features Comparison

| Feature | Console | GUI |
|---------|---------|-----|
| Add Student | ✅ | ✅ |
| View Student  | ✅ | ✅ |
| Update Student | ✅ | ✅ |
| Delete Student | ✅ | ✅ |
| Search         | ❌ | ✅ |
| Statistics     | ❌ | ✅ |
| Export CSV     | ❌ | ✅ |
| Modern UI      | ❌ | ✅ |
| File Persistence | ❌ | ✅ |
| Grade Calculation | ❌ | ✅ |

## Future Enhancements
- User authentication and login
- Database support (MySQL, PostgreSQL)
- PDF report generation
- Email notifications
- Photo upload for students
- Performance charts and analytics
- Backup and restore functionality

## License
Free to use and modify

## Author
Created with ❤️ for educational purposes

---

**Note**: This application was created to provide a complete student management solution with file handling, advanced features, and a modern GUI interface.
