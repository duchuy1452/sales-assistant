"""
Chat handler for AI Assistant
"""

import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatHandler:
    """Handles chat interactions with Gemini AI"""
    
    def __init__(self) -> None:
        """Initialize the chat handler"""
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in environment variables")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        logger.info("Chat handler initialized successfully")
    
    def get_response(self, message: str) -> str:
        """Get response from AI model
        
        Args:
            message: User input message
            
        Returns:
            AI response as string
        """
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
    
    def validate_api_key(self) -> bool:
        """Validate if API key is properly configured
        
        Returns:
            True if API key is valid, False otherwise
        """
        return bool(GEMINI_API_KEY and GEMINI_API_KEY != "your_api_key_here") 