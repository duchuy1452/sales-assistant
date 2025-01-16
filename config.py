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
APP_TITLE = "AI Sales Strategy Assistant"
PAGE_TITLE = "AI Sales Strategy Assistant"

# Sales Strategy Questions
PREDEFINED_QUESTIONS = [
    "How can I improve my sales conversion rates?",
    "What are effective lead generation strategies?",
    "How do I build a strong sales funnel?",
    "What are the best customer retention techniques?",
    "How should I price my products competitively?",
    "What sales metrics should I track?",
    "How can I build an effective sales team?",
    "What are common sales objections and how to handle them?",
    "How do I optimize my CRM system?",
    "What are effective upselling and cross-selling strategies?",
] 