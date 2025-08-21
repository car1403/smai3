import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
#GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]


def geminiModel():
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
    return model

def geminiTxt(txt):
    model = geminiModel()
    response = model.generate_content(txt)
    return response.text

