
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
#from langchain_community.chat_models import ChatAnthropic
from openai import OpenAIError, RateLimitError
from langchain_anthropic import ChatAnthropic
import os
from langchain_core.messages import SystemMessage, HumanMessage
#import streamlit   as st
# Load environment variables (including API keys)
load_dotenv()


llm_name  = "claude-3-opus-20240229"
models = ChatAnthropic(model=llm_name)

messages = [
    SystemMessage (
        content= "You are a helpful assistant that helps the user to decide on what to buy from an application and also on the gifts to gift dear friends. Your name is Peace "
    ),
    #HumanMessage ("What can I get for my friend who is a software engineer and loves to play video games?"),
]
#response = models.invoke(messages)
#print("Claude response:", response.content)

#function for users to interract with the model
def chat_with_model(messages):
    try:
        # Call the model with the messages
        response = models.invoke(messages)
        return response.content
    except OpenAIError as e:
        print(f"OpenAI API error: {e}")
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_chat():
    # Example usage
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting the chat.")
            break
        # messages = [
        #     #SystemMessage,
        #     HumanMessage(content=user_input)]        
        messages.append(HumanMessage(content=user_input))
        response = chat_with_model(messages)
        print("Assistant getting response, wait for a moment...")
        print("Assistant:", response)
   
if __name__ == "__main__":
    # Run the chat function
    run_chat()
# The code is a simple chat application that interacts with the Claude AI model using the LangChain library.
  
# st.title("Chat with Peace Your Shopping Assistance")
# st.write("Ask me anything about shopping and gifts!")