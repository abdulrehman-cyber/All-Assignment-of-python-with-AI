@echo off
REM Student Management System - Web App Launcher

echo.
echo ========================================
echo Student Management System - Web App
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Start the Flask app
echo.
echo Starting Student Management System...
echo.
echo 🚀 Application is running!
echo 📍 Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python web_app.py

pause
