import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
# from dotenv import load_dotenv
# load_dotenv()

# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")#
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot with groq"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are an helpful ai assistant. please respond to the user questions"),
        ("user","Question:{question}")
    ]
)


def generate_response(question,api_key,llm_model):
    llm=ChatGroq(model=llm_model,api_key=api_key)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer


st.title("Q & A chatbot with groq")
api_key=st.sidebar.text_input("Enter your Groq api key:",type="password")

llm_model=st.sidebar.selectbox("select groq model",["llama-3.1-8b-instant","openai/gpt-oss-20b"])


st.write("Go ahead and ask any question")

user_input=st.text_input("you:")

if user_input and api_key:
    response=generate_response(user_input,api_key,llm_model)
    st.write(response)

elif user_input:
    st.warning("Please enter the Groq api Key in the side bar")
else:
    st.write("Please provide the user input")

    