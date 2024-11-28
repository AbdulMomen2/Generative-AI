import requests
import streamlit as st

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/seo/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output'] ['topic']

st.title('Langchain Demo With LLAMA3.2-vision API')
input_text=st.text_input("Write an article on")

if input_text:
    st.write(get_ollama_response(input_text))