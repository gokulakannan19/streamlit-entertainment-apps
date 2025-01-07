import streamlit as st
from modules import backend

st.title("Flames")

with st.form(key="input-form"):
    name1 = st.text_input("Enter your name: ")
    name2 = st.text_input("Enter your partner name: ")
    button = st.form_submit_button("Put Flames")

    if button:
        result = backend.put_flames(name1, name2)
        st.info(result)

