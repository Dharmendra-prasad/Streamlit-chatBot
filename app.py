import streamlit as st
import os
import google.generativeai as genai

st.title('Chat - Gemini Bot')

os.environ['GOOGLE_API_KEY'] = "AIzaSyDZKvJ7Ja-g6Xf26d7wU22NL8GAkXorTD4"

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me Anything"
        }
    ]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def llm_function(query):
    response = model.generate_content(query)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistent",
            "content": response.text
        }
    )

query = st.chat_input("What is up?")

if(query):
    with st.chat_message("user"):
        st.markdown(query)

    llm_function(query)    