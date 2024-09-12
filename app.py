# Question and answer appfrom lang
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os


# function to lead the openao model and will give us responses 

def openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),temperature=0.5)
    response=llm(question)
    return response

# intializing the streamlit app

st.title("Question and Answer App")
st.header("Langchain Model")

# taking input from the user
input=st.text_input("Enter to ask ",key="input")
response=openai_response(input)

submit=st.button("Ask")

# if ask button is pressed 

if submit:
 st.subheader("Here, is your answer")
 st.write(response)

