import streamlit as st
from modules import backend

st.title("Rock Paper Scissor")

with st.form(key="rock-form"):
    player_input = st.selectbox("Select your input",
                                ["Rock", "Paper", "Scissor", "Exit"])
    button = st.form_submit_button("Done")

    if button:
        computer_choice = backend.rock_paper_scissor(player_input)
        st.info(f"computer_choice: {computer_choice}")
        st.success("You win")

col1, col2, col3 = st.columns([1.5, 0.5, 1.5])
with col1:
    with st.container():

        st.subheader("Your Score")
        st.markdown(f"""
            <div style="background-color: #c8e6c9; padding: 10px; border-radius: 5px;">
                Score: 95
            </div>
            """, unsafe_allow_html=True)

with col3:
    with st.container():

        st.subheader("Computer Score")
        st.markdown(f"""
            <div style="background-color: #c8e6c9; padding: 10px; border-radius: 5px;">
                Score: 95
            </div>
            """, unsafe_allow_html=True)