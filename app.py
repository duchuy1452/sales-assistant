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
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize chat handler
    chat_handler = ChatHandler()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_handler.get_response(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main() 