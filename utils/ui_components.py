"""
UI Components for AI Assistant
"""

import streamlit as st

def load_css():
    """Load custom CSS styles"""
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .chat-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .question-button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0.2rem;
        cursor: pointer;
    }
    
    .question-button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

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
    st.markdown("""
    <div class="main-header">
        <h2>Welcome to AI Assistant!</h2>
        <p>Ask me anything or choose from the suggested questions below.</p>
    </div>
    """, unsafe_allow_html=True) 