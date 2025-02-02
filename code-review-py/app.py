from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
import streamlit as st
from dotenv import load_dotenv
import time
import base64
import os

load_dotenv()

st.title("Let's do code review for your Python code")
st.header("Please upload your .py file here:")

def text_downloader(raw_text):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = f"code_review_analysis_{timestr}.txt"
    st.markdown("#### Download File ✅")
    href = f'<a href="data:file/text;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    st.markdown(href, unsafe_allow_html=True)


data = st.file_uploader("Upload Python file", type=".py")

if data:
   
    fetched_data = data.getvalue().decode("utf-8")
    st.write("### Uploaded File Content:")
    st.code(fetched_data, language='python')

 
    chat = ChatGroq(
        temperature=0.7,
        model_name="deepseek-r1-distill-llama-70b",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    system_message = SystemMessage(content=(
    "You are a highly skilled code review assistant. Analyze the provided Python code line by line, "
    "offering detailed suggestions for improvement. Identify potential bugs, performance issues, security risks, "
    "and adherence to best practices. Ensure that your feedback includes:"
    "\n- The specific line(s) of code being reviewed."
    "\n- Clear explanations of issues or improvements."
    "\n- Suggested modifications with proper indentation."
    "\n- Relevant references to Pythonic best practices."
    ))
    human_message = HumanMessage(content=fetched_data)

    final_response = chat([system_message, human_message])

    st.write("### Code Review Suggestions:")
    st.markdown(final_response.content)

    text_downloader(final_response.content)