import os
import pandas as pd
from langchain_community.llms import openai
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI()

df = pd.read_csv("Financials.csv")

sdf = SmartDataframe(df, config={"llm": llm})

print(sdf.chat("Describe data"))

print(sdf.chat("info of data"))

print(sdf.last_code_generated)

print(sdf.chat("displace the relation between  Manufacturing Price and  Sale Price "))

print(sdf.last_code_generated)
