from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage
import streamlit as st
import os

# Load environment variables
load_dotenv()

# Claude model setup
llm_name = "claude-3-opus-20240229"
model = ChatAnthropic(model=llm_name)

# Streamlit UI
st.title("🛍️ Chat with Peace – Your Shopping Assistant")
st.write("Ask Peace what to buy for birthdays, events, or gift ideas!")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(
            content="You are a helpful assistant that helps the user decide what to buy from an e-commerce application and what gifts to give to dear friends. Your name is Peace."
        )
    ]

# User input
#user_input = st.text_input("You:", key="input")
user_input = st.text_area("You:", key="input", height=100)


# Submit button
if st.button("Send") and user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    try:
        with st.spinner("Peace is thinking..."):
            response = model.invoke(st.session_state.chat_history)
            st.session_state.chat_history.append(response)
            st.success("Response received!")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display conversation history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.markdown(f"**You:** {msg.content}")
    elif isinstance(msg, SystemMessage):
        st.markdown(f"🛠️ *System Instruction*: {msg.content}")
    else:
        st.markdown(f"**Peace:** {msg.content}")
# Add a footer
st.markdown(
    """
    ---
    Made with ❤️ by Adejoke Ogundipe
    """
)

#can you add a function to read from a ecommerce site and get the product suggestions

# The code is a simple chat application that interacts with the Claude AI model using the LangChain library.
# It allows users to ask questions about shopping and gift ideas.
# The chat history is maintained in the session state, and the user can input their queries through a text area.