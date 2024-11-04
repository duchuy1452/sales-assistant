"""
Chat handler for AI Assistant
"""

import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatHandler:
    """Handles chat interactions with Gemini AI"""
    
    def __init__(self):
        """Initialize the chat handler"""
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in environment variables")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        logger.info("Chat handler initialized successfully")
    
    def get_response(self, message: str) -> str:
        """Get response from AI model"""
        if not message.strip():
            return "Please enter a valid message."
        
        try:
            logger.info(f"Generating response for message: {message[:50]}...")
            response = self.model.generate_content(message)
            
            if response.text:
                logger.info("Response generated successfully")
                return response.text
            else:
                logger.warning("Empty response from model")
                return "I'm sorry, I couldn't generate a response. Please try again."
                
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return f"I'm sorry, I encountered an error: {str(e)}" 