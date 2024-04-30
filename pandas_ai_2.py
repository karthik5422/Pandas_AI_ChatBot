import os
import openai
import pandas as pd
import streamlit as st
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0)

st.title('PANDAS AI')

upload_file = st.file_uploader('Upload arquivo CSV para análise', type=['csv'])

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df.head())

    # convert to SmartDataframe
    sdf = SmartDataframe(df, config={"llm": llm})

    prompt = st.text_area('Prompt')

    if st.button('Enter'):
        if prompt:
            with st.spinner('Enter your qurstion'):
                response = sdf.chat(prompt)
                st.success(response)

                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()
        else:
            st.warning('Enter prompt')