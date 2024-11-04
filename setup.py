#!/usr/bin/env python3
"""
Setup script for AI Assistant
"""

import subprocess
import sys
import venv
from pathlib import Path

def main():
    """Main setup function"""
    print("=" * 40)
    print("AI Assistant - Setup")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8+ required")
        sys.exit(1)
    
    print("Python version:", sys.version.split()[0])
    
    # Create virtual environment
    venv_path = Path("venv")
    if not venv_path.exists():
        print("Creating virtual environment...")
        venv.create(venv_path, with_pip=True)
    
    # Install dependencies
    print("Installing dependencies...")
    subprocess.check_call(["venv/bin/pip", "install", "-r", "requirements.txt"])
    
    # Setup environment
    if not Path(".env").exists():
        print("Creating .env file...")
        with open(".env", "w") as f:
            f.write("GEMINI_API_KEY=your_api_key_here\n")
    
    print("\nSetup completed!")
    print("1. Activate virtual environment: source venv/bin/activate")
    print("2. Add your API key to .env file")
    print("3. Run: streamlit run app.py")

if __name__ == "__main__":
    main() 