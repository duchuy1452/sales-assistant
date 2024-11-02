"""
Configuration settings for AI Assistant
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.0-flash-exp"

# App Configuration
APP_TITLE = "AI Assistant"
PAGE_TITLE = "AI Assistant" 