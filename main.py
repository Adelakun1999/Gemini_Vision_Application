import os 

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

openai = os.getenv('GOOGLE_API_KEY')

import google.generativeai as genai

genai.configure(api_key =openai )

model = genai.GenerativeModel('gemini-pro')


def model_question(question):
    response = model.generate_content(question)
    return response.text


def lang(message):
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.9)
    response = llm.invoke(message)
    
    return response.content

import streamlit as st
st.set_page_config(page_title="q&a demo")
st.header('Gemini Application')

text = st.text_input('Ask any question : ')

if st.button('Answer'):
    output = model_question(text)
    st.subheader('The response of the LLM model is :  ')
    st.write(output)
