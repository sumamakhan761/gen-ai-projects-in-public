import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot project"

# prompts
prompt=ChatPromptTemplate(
  [
    ("system","You are a helpful assistant. Please response to the user queries"),
    ("user","Question:{question}")
  ]
)

def generate_response(question, api_key, llm,temperature, max_tokens):
  openai.api_key = api_key
  llm = ChatOpenAI(model=llm)
  output_parser = StrOutputParser()
  chain=prompt|output_parser
  answer = chain.invoke({"question":question})
  return answer

st.title("OpenAI Chatbot")
# side bar
st.sidebar.title("Settings")

api_key=st.sidebar.text_input("Enter your Open API key", type="password")

llm=st.sidebar.selectbox("Select OpenAI model", ["gpt-40", "gpt-4-turbo","gpt-4"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Token",min_value=50,max_value=300, value=150)

# main interface user input

st.write("Enter your Question")
user_input=st.text_input("You:")

if user_input:
  response=generate_response(user_input, api_key, llm, temperature, max_tokens)
  st.write(response)
else:
  st.write("Please enter a question")