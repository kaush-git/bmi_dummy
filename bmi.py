import streamlit as st 
import google.generativeai as genai 
import pandas as pd
import os 
from dotenv import load_dotenv
load_dotenv() 
# configuring API
key_variable = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = key_variable)


# set up our page
st.title('HEALTH ASSISTANT FOR FITNESS🚀')
st.subheader('This page will help you to get information for fitness using BMI values')

st.sidebar.subheader('Height:')
height = st.sidebar.text_input('Enter the Height in meters')

st.sidebar.subheader('Weight:')
weight = st.sidebar.text_input('Enter the Weight in meters')

# calculating BMI values
try:
    height = pd.to_numeric(height)
    weight = pd.to_numeric(weight)
    if height > 0 and weight > 0:
        bmi = round(weight / (height**2),2)
        st.sidebar.success(f'BMI values is: {bmi}')
    else:
        st.write('Please enter positive values.')
except:
    st.sidebar.info('Please enter positive values')
input = st.text_input('Ask your question here❗')
submit = st.button('Click here❗')
model = genai.GenerativeModel('gemini-1.5-flash')

def generative_result(bmi,input):    
    if input is not None:
        prompt = f'''
        You are a health assistant now. Give me suggestions based on the bmi value {bmi}. give me some diet suggestions. 
        '''
        result = model.generate_content(input+prompt)
        return result.text
if submit:
    with st.spinner('Result is loading.......'):
        response = generative_result(bmi,input)
        
        st.markdown(':green[Result]')
        st.write(response)