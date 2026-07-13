#!/usr/bin/env python3
"""
Student Management System - Launcher Script
This script starts the GUI application
"""

import sys
import os

try:
    from gui_app import StudentManagementGUI
    import tkinter as tk
    
    print("🚀 Starting Student Management System...")
    
    root = tk.Tk()
    app = StudentManagementGUI(root)
    root.mainloop()
    
except ImportError as e:
    print(f"❌ Error: Required module not found - {e}")
    print("Please ensure all files are in the same directory")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error starting application: {e}")
    sys.exit(1)
