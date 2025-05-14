import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st

# Load environment variables
load_dotenv()
model = ChatAnthropic(model="claude-3-opus-20240229")

# Streamlit config
st.set_page_config(
    page_title="Tech Guru",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Sidebar
st.sidebar.title("Tech Guru")
st.sidebar.image("https://your-logo-url.com/logo.png", width=200)
st.sidebar.write("Welcome to Tech Guru! Ask me anything about tech and programming.")
st.sidebar.title("📜 Chat History")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(
            content="You are a helpful assistant that helps the user learn programming and everything related to tech from scratch to advanced level. Your name is Tech Guru."
        )
    ]

# Sidebar compact preview of last message only
if len(st.session_state.chat_history) > 1:
    last_msg = st.session_state.chat_history[-1]
    if isinstance(last_msg, HumanMessage):
        st.sidebar.markdown(f"🧑‍💻 {last_msg.content[:20]}...")
    elif isinstance(last_msg, AIMessage):
        st.sidebar.markdown(f"🤖 {last_msg.content[:20]}...")

# Main Title
st.header("🛠️ Tech Guru – Your Personal Tech Tutor")

# Input field
user_input = st.text_area("You:", key="input", height=100)

# Submit and get AI response
if st.button("Send") and user_input:
    # Add the user input to the chat history (but only for the current message)
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Get the response from the AI model
    with st.spinner("Tech Guru is thinking..."):
        try:
            # Get the latest response
            response = model.invoke([st.session_state.chat_history[-1]])
            st.session_state.chat_history.append(response)
        except Exception as e:
            st.error(f"Error: {e}")

    # Show only the latest response (don't append entire history)
    latest_msg = st.session_state.chat_history[-1]
    if isinstance(latest_msg, AIMessage):
        st.markdown(f"**Tech Guru:** {latest_msg.content}")

# Footer
st.markdown("---\nMade with ❤️ by Adejoke Ogundipe")
