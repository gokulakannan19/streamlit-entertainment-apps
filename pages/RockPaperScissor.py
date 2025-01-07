import streamlit as st

st.title("Rock Paper Scissor")

with st.form(key="rock-form"):
    player_input = st.selectbox("Select your input",
                                ["Rock", "Paper", "Scissor", "Exit"])
    button = st.form_submit_button("Done")

    if button:
        pass