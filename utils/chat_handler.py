"""
Chat handler for AI Assistant
"""

import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

class ChatHandler:
    """Handles chat interactions with Gemini AI"""
    
    def __init__(self):
        """Initialize the chat handler"""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
    
    def get_response(self, message: str) -> str:
        """Get response from AI model"""
        try:
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}" 