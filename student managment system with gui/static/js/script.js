// Student Management System - Frontend JavaScript

// DOM Elements
const studentForm = document.getElementById('studentForm');
const studentsList = document.getElementById('studentsList');
const alertContainer = document.getElementById('alertContainer');
const loadingSpinner = document.getElementById('loadingSpinner');
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const clearBtn = document.getElementById('clearBtn');
const editModal = new bootstrap.Modal(document.getElementById('editModal'));
const statsModal = new bootstrap.Modal(document.getElementById('statsModal'));
const editForm = document.getElementById('editForm');
const saveChangesBtn = document.getElementById('saveChangesBtn');
const statsBtn = document.getElementById('statsBtn');

// State
let allStudents = [];
let currentEditId = null;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    loadStudents();
    setupEventListeners();
});

// Setup Event Listeners
function setupEventListeners() {
    studentForm.addEventListener('submit', handleAddStudent);
    searchBtn.addEventListener('click', handleSearch);
    clearBtn.addEventListener('click', handleClear);
    saveChangesBtn.addEventListener('click', handleSaveChanges);
    statsBtn.addEventListener('click', loadStats);
}

// Load all students
function loadStudents() {
    showLoading(true);
    fetch('/api/students')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                allStudents = data.data;
                renderStudents(allStudents);
            } else {
                showAlert('Error loading students: ' + data.error, 'danger');
            }
        })
        .catch(error => {
            showAlert('Error loading students: ' + error.message, 'danger');
        })
        .finally(() => showLoading(false));
}

// Render students in table
function renderStudents(students) {
    if (students.length === 0) {
        studentsList.innerHTML = `
            <tr>
                <td colspan="9" class="text-center text-muted py-4">
                    <i class="fas fa-inbox"></i> No students found. Add one to get started!
                </td>
            </tr>
        `;
        return;
    }

    studentsList.innerHTML = students.map(student => `
        <tr>
            <td><strong>${student.roll_no}</strong></td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.marks}</td>
            <td><span class="badge" style="background-color: ${getGradeColor(student.grade)}">${student.grade}</span></td>
            <td>
                <span class="badge ${student.status === 'Pass' ? 'pass' : 'fail'}">
                    ${student.status}
                </span>
            </td>
            <td>${student.email || '-'}</td>
            <td>${student.phone || '-'}</td>
            <td>
                <div class="action-buttons">
                    <button class="btn btn-warning btn-sm" onclick="openEditModal(${student.id})">
                        <i class="fas fa-edit"></i> Edit
                    </button>
                    <button class="btn btn-danger btn-sm" onclick="deleteStudent(${student.id})">
                        <i class="fas fa-trash"></i> Delete
                    </button>
                </div>
            </td>
        </tr>
    `).join('');
}

// Get color for grade
function getGradeColor(grade) {
    const colors = {
        'A+': '#28a745',
        'A': '#28a745',
        'B': '#17a2b8',
        'C': '#ffc107',
        'D': '#fd7e14',
        'F': '#dc3545'
    };
    return colors[grade] || '#6c757d';
}

// Handle add student
function handleAddStudent(e) {
    e.preventDefault();

    const formData = {
        roll_no: parseInt(document.getElementById('rollNo').value),
        name: document.getElementById('name').value,
        age: parseInt(document.getElementById('age').value),
        marks: parseFloat(document.getElementById('marks').value),
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value
    };

    showLoading(true);
    fetch('/api/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showAlert(data.message, 'success');
                studentForm.reset();
                loadStudents();
            } else {
                showAlert('Error: ' + data.error, 'danger');
            }
        })
        .catch(error => {
            showAlert('Error adding student: ' + error.message, 'danger');
        })
        .finally(() => showLoading(false));
}

// Open edit modal
function openEditModal(studentId) {
    const student = allStudents.find(s => s.id === studentId);
    if (!student) return;

    currentEditId = studentId;
    document.getElementById('editId').value = studentId;
    document.getElementById('editName').value = student.name;
    document.getElementById('editAge').value = student.age;
    document.getElementById('editMarks').value = student.marks;
    document.getElementById('editEmail').value = student.email;
    document.getElementById('editPhone').value = student.phone;

    editModal.show();
}

// Handle save changes
function handleSaveChanges() {
    const updateData = {
        name: document.getElementById('editName').value,
        age: parseInt(document.getElementById('editAge').value),
        marks: parseFloat(document.getElementById('editMarks').value),
        email: document.getElementById('editEmail').value,
        phone: document.getElementById('editPhone').value
    };

    showLoading(true);
    fetch(`/api/students/${currentEditId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updateData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showAlert(data.message, 'success');
                editModal.hide();
                loadStudents();
            } else {
                showAlert('Error: ' + data.error, 'danger');
            }
        })
        .catch(error => {
            showAlert('Error updating student: ' + error.message, 'danger');
        })
        .finally(() => showLoading(false));
}

// Delete student
function deleteStudent(studentId) {
    if (!confirm('Are you sure you want to delete this student?')) return;

    showLoading(true);
    fetch(`/api/students/${studentId}`, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showAlert(data.message, 'success');
                loadStudents();
            } else {
                showAlert('Error: ' + data.error, 'danger');
            }
        })
        .catch(error => {
            showAlert('Error deleting student: ' + error.message, 'danger');
        })
        .finally(() => showLoading(false));
}

// Handle search
function handleSearch() {
    const query = searchInput.value.trim();
    if (!query) {
        showAlert('Please enter a search query', 'warning');
        return;
    }

    showLoading(true);
    fetch(`/api/search?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                renderStudents(data.data);
                if (data.count === 0) {
                    showAlert(`No students found for "${query}"`, 'info');
                }
            } else {
                showAlert('Error: ' + data.error, 'danger');
            }
        })
        .catch(error => {
            showAlert('Error searching: ' + error.message, 'danger');
        })
        .finally(() => showLoading(false));
}

// Handle clear search
function handleClear() {
    searchInput.value = '';
    loadStudents();
    showAlert('Search cleared', 'info');
}

// Load statistics
function loadStats() {
    showLoading(true);
    fetch('/api/stats')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const stats = data.data;
                document.getElementById('totalStudents').textContent = stats.total_students;
                document.getElementById('avgMarks').textContent = stats.avg_marks.toFixed(2);
                document.getElementById('passedCount').textContent = stats.passed;
                document.getElementById('failedCount').textContent = stats.failed;
                statsModal.show();
            } else {
                showAlert('Error loading stats: ' + data.error, 'danger');
            }
        })
        .catch(error => {
            showAlert('Error loading stats: ' + error.message, 'danger');
        })
        .finally(() => showLoading(false));
}

// Show alert message
function showAlert(message, type = 'info') {
    const alertId = 'alert-' + Date.now();
    const alertHTML = `
        <div class="alert alert-${type} alert-dismissible fade show" id="${alertId}" role="alert">
            <i class="fas fa-${getAlertIcon(type)}"></i> ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;

    alertContainer.insertAdjacentHTML('beforeend', alertHTML);

    // Auto remove after 5 seconds
    setTimeout(() => {
        const alert = document.getElementById(alertId);
        if (alert) {
            alert.remove();
        }
    }, 5000);
}

// Get icon for alert
function getAlertIcon(type) {
    const icons = {
        'success': 'check-circle',
        'danger': 'exclamation-circle',
        'warning': 'exclamation-triangle',
        'info': 'info-circle'
    };
    return icons[type] || 'info-circle';
}

// Show/hide loading spinner
function showLoading(show) {
    if (show) {
        loadingSpinner.classList.remove('d-none');
    } else {
        loadingSpinner.classList.add('d-none');
    }
}
