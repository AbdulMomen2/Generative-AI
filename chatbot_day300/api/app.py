from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os
from dotenv import load_dotenv


load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI (
    title = "Langchain Server",
    version = "1.0",
    description = "First Api sever"
)

llm = Ollama(model ="llama3.2-vision")

prompt= ChatPromptTemplate.from_template("Write a seo friendly article on {topic} max 100 words")

add_routes(
    app,
    prompt|llm,
    path = "/seo"
    
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
