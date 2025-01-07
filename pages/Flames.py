import streamlit as st

st.title("Flames")

with st.form(key="input-form"):
    name1 = st.text_input("Enter your name: ")
    name2 = st.text_input("Enter your partner name: ")
    st.form_submit_button("Put Flames")
