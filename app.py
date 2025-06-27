import streamlit as st
import requests
import json

st.set_page_config(
    page_title="AI Career Counselor",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []

def send_message(message):
    """Send a message to Rasa and get the response"""
    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": message},
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error from chatbot server: {response.status_code}")
            return []
    except requests.exceptions.Timeout:
        st.error("Request timed out. Please check if the Rasa server is running.")
        return []
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the Rasa server. Please make sure it's running on port 5005.")
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with the chatbot: {str(e)}")
        return []

# Main UI
st.title("🎓 AI Career Counselor")

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.write("""
    Welcome to the AI Career Counselor! 
    
    This tool helps you:
    - Explore career paths based on your interests
    - Learn about required skills
    - Understand educational requirements
    - Get insights about job prospects
    - Learn about salary ranges
    """)
    
    st.header("Sample Questions")
    st.write("""
    Try asking:
    - "What career should I choose?"
    - "I like working with computers"
    - "What skills do I need for software development?"
    - "Tell me about job prospects in data science"
    - "What's the salary range for UX design?"
    """)

# Chat interface
st.header("Chat with your Career Counselor")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write("You:", message["content"])
    else:
        st.write("Career Counselor:", message["content"])

# Chat input
with st.form(key='chat_form'):
    prompt = st.text_input("Type your message here...", key="chat_input")
    submit_button = st.form_submit_button(label='Send')

    if submit_button and prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get bot response
        responses = send_message(prompt)
        
        if responses:
            # Add bot response to chat history
            for response in responses:
                message = response.get('text', 'Sorry, I did not understand that.')
                st.session_state.messages.append({"role": "assistant", "content": message})
        else:
            # Add fallback message if Rasa returns an empty response
            st.session_state.messages.append({
                "role": "assistant", 
                "content": "I'm not sure how to answer that yet, but I'm learning! Please try rephrasing your question or ask about another career topic."
            })

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with ❤️ by Your AI Career Counselor</p>
    </div>
    """,
    unsafe_allow_html=True)
