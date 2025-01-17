"""
UI Components for AI Assistant
"""

import streamlit as st
from config import PREDEFINED_QUESTIONS

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
        width: 100%;
        text-align: left;
    }
    
    .question-button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render sidebar with app info and questions"""
    with st.sidebar:
        st.header("About")
        st.write("AI Sales Strategy Assistant powered by Google Gemini")
        st.write("Built with Streamlit")
        
        st.divider()
        
        # Sales Strategy Questions in sidebar
        st.subheader("Sales Strategy Questions")
        st.write("Click any question to get started:")
        
        for i, question in enumerate(PREDEFINED_QUESTIONS):
            if st.button(question, key=f"sidebar_q_{i}", help="Click to ask this question"):
                return question  # Return the selected question
        
        st.divider()
        
        if st.button("Clear Chat", type="secondary"):
            st.session_state.messages = []
            st.rerun()
    
    return None  # No question selected

def render_chat_input():
    """Render chat input field"""
    return st.chat_input("Ask me anything about sales strategy...")

def render_welcome_message():
    """Render welcome message"""
    st.markdown("""
    <div class="main-header">
        <h2>Welcome to AI Sales Strategy Assistant!</h2>
        <p>Choose a question from the sidebar or type your own question below.</p>
    </div>
    """, unsafe_allow_html=True) 