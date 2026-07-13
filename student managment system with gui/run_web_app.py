#!/usr/bin/env python3
"""
Student Management System - Web App Launcher
Run this script to start the Flask web application
"""

import sys
import subprocess
import os

def main():
    print("\n" + "="*50)
    print("Student Management System - Web App")
    print("="*50 + "\n")
    
    # Check if Flask is installed
    try:
        import flask
        import flask_sqlalchemy
    except ImportError:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("\n✅ All dependencies installed!\n")
    print("🚀 Starting Student Management System...")
    print("📍 Open your browser and go to: http://localhost:5000\n")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        from web_app import app
        app.run(debug=True, port=5000)
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        print("\nPlease make sure all files are in the same directory:")
        print("  - web_app.py")
        print("  - requirements.txt")
        print("  - templates/index.html")
        print("  - static/css/style.css")
        print("  - static/js/script.js")
        sys.exit(1)

if __name__ == "__main__":
    main()
