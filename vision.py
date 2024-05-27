import os 

from dotenv import load_dotenv, find_dotenv

from PIL import Image

load_dotenv(find_dotenv(), override=True)

openai = os.getenv('GOOGLE_API_KEY')

import google.generativeai as genai

genai.configure(api_key =openai )

model = genai.GenerativeModel('gemini-pro-vision')


def model_question(input, image):
    if input !="":
        response = model.generate_content([input,image])

    else : 
        response = model.generate_content(image)


    return response.text


import streamlit as st 

st.set_page_config(page_title='Gemini Image Demo')
st.header('Gemini Application')

input = st.text_input('Input Prompt : ')

uploaded_file = st.file_uploader('Choose an image', 
                                 type=['jpg','jpeg','png'])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='uploaded Image', use_column_width=True)


submit = st.button("Tell me about the image")
if submit :
    response = model_question(input, image)
    st.subheader('The response is')
    st.write(response)


