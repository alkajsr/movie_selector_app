# Personal Movie-Suggestor

import streamlit as st
import google.genai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
     API_KEY = st.secrets["API_KEY"]

if not API_KEY:
     st.error("API Key missing")

client = genai.Client(api_key = API_KEY)

st.title('AI Personal Movies/Dramas Suggestor🎬')

st.markdown("""
    <style>
    .stApp {
    background:linear-gradient(to right,#7cd4f7c0,#E8F5E9)}
     </style>
     """,unsafe_allow_html=True)

with st.form(key="movie_form", clear_on_submit=True):
      user = st.text_input("Your name")
      no = st.slider("Total Number of Movies to choose from:",1,10)
      genre = st.selectbox("Select Genre", ["Comedy", "Romantic", "Action","Drama","Slice of Life","Fantasy","Adventure","Horror",])
      type = st.selectbox("Select Type", ["Movies", "Dramas", "Movies and Dramas"])
      language = st.selectbox("Select Language",["English","Hindi","Japanese","Chinese","Korean","Telugu","Tamil"])
      submitted = st.form_submit_button("**Generate Recommendations**",type="primary")

if submitted and user and no and genre and type and language and submitted:
    st.write(f"Hey {user}😊, Your recommendations are on the way...")
    prompt = f"Suggest total only {no} {type}, genre should be {genre} and should be of {language} language. Also suggest ott platforms where one can watch them. Keep it crisp and simple in about 100-200 words. Use friendly tone to communicate."
    response = client.models.generate_content(
            model = "gemini-3.5-flash-lite",
            contents = prompt
            )
    st.write(response.text)
    if st.button("Clear"):
       st.session_state.response  =""
       st.rerun()
elif submitted:
   st.text("Please enter all the details")