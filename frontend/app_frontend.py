# frontend/app_frontend.py
import streamlit as st
import requests

st.title("Chatbot Interface")

user_input = st.text_input("You:", "")

if st.button("Send"):
    response = requests.post("http://backend:8000/api/chat", json={"message": user_input})
    st.write("Bot:", response.json().get("reply"))