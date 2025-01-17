"""
AI Sales Strategy Assistant - Streamlit App
"""

import streamlit as st
from config import APP_TITLE, PAGE_TITLE
from utils.chat_handler import ChatHandler
from utils.ui_components import render_sidebar, render_chat_input, render_welcome_message, load_css

def main():
    """Main application function"""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon="💼",
        layout="wide"
    )
    
    # Load custom CSS
    load_css()
    
    st.title(APP_TITLE)
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize chat handler
    try:
        chat_handler = ChatHandler()
        
        # Render sidebar and get selected question
        selected_question = render_sidebar()
        
        # Handle selected question from sidebar
        if selected_question:
            st.session_state.messages.append({"role": "user", "content": selected_question})
            with st.spinner("Analyzing your sales strategy..."):
                response = chat_handler.get_response(selected_question)
                st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        # Welcome message for new users
        if not st.session_state.messages:
            render_welcome_message()
        
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := render_chat_input():
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Get AI response
            with st.chat_message("assistant"):
                with st.spinner("Analyzing your sales strategy..."):
                    response = chat_handler.get_response(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
    except ValueError as e:
        st.error(f"Configuration Error: {e}")
        st.info("Please check your .env file and ensure GEMINI_API_KEY is set correctly.")

if __name__ == "__main__":
    main() 