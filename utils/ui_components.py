"""
UI Components for AI Assistant
"""

import streamlit as st

def render_sidebar():
    """Render sidebar with app info"""
    with st.sidebar:
        st.header("About")
        st.write("AI Assistant powered by Google Gemini")
        st.write("Built with Streamlit")
        
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()

def render_chat_input():
    """Render chat input field"""
    return st.chat_input("Ask me anything...")

def render_welcome_message():
    """Render welcome message"""
    st.write("Welcome to AI Assistant!")
    st.write("Ask me anything or choose from the suggested questions below.") 