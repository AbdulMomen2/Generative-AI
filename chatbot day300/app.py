from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set environment variables for LangChain
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Streamlit Framework
st.title('LangChain Demo with LLAMA 3.2 API')
input_text = st.text_input("Enter your query:")

# LLM Setup
llm = Ollama(model="llama3.2-vision")
chain = LLMChain(prompt=prompt, llm=llm)

# Query Handling
if input_text:
    try:
        response = chain.run({"question": input_text})
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
