@echo off
REM Student Management System - Launcher
REM This script will start the GUI application

python gui_app.py

if errorlevel 1 (
    echo.
    echo Error: Could not start the application
    echo Please ensure Python is installed and in your PATH
    pause
)
