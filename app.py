"""
AI Assistant - Streamlit App
"""

import streamlit as st
from config import APP_TITLE, PAGE_TITLE
from utils.chat_handler import ChatHandler

def main():
    """Main application function"""
    st.set_page_config(
        page_title=PAGE_TITLE,
        layout="wide"
    )
    
    st.title(APP_TITLE)
    st.write("Welcome to AI Assistant!")
    
    # Initialize chat handler
    chat_handler = ChatHandler()
    
    # Simple chat interface
    user_input = st.text_input("Ask me anything:")
    
    if user_input:
        with st.spinner("Thinking..."):
            response = chat_handler.get_response(user_input)
            st.write(response)

if __name__ == "__main__":
    main() 