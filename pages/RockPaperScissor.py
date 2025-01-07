import streamlit as st
from modules import backend


st.title("Rock Paper Scissor")

if "user_score" not in st.session_state:
    st.session_state["user_score"] = 0
if "computer_score" not in st.session_state:
    st.session_state["computer_score"] = 0

def update_score(result_local):
    if result_local == "user":
        st.session_state.user_score = backend.add_score(st.session_state.user_score)
    elif result_local == "computer":
        st.session_state.computer_score = backend.add_score(st.session_state.computer_score)
    else:
        pass


with st.form(key="rock-form"):
    player_input = st.selectbox("Select your input",
                                ["Rock", "Paper", "Scissor", "Exit"])
    button = st.form_submit_button("Done")

    if button:
        computer_choice, result = backend.rock_paper_scissor(player_input)
        col4, col5, col6 = st.columns([1.5, 0.5, 1.5])
        with col4:
            st.warning(f"user_choice: {player_input}")
        with col6:
            st.warning(f"computer_choice: {computer_choice}")

        if result == "user":
            st.success("You win")
        elif result == "computer":
            st.error("Computer win")
        else:
            st.info("Draw")

        update_score(result)

col1, col2, col3 = st.columns([1.5, 0.5, 1.5])
with col1:
    with st.container():

        st.subheader("Your Score")
        st.markdown(f"""
            <div style="background-color: #c8e6c9; padding: 10px; border-radius: 5px;">
                Score: {st.session_state.user_score}
            </div>
            """, unsafe_allow_html=True)

with col3:
    with st.container():

        st.subheader("Computer Score")
        st.markdown(f"""
            <div style="background-color: #FF7F7F; padding: 10px; border-radius: 5px;">
                Score: {st.session_state.computer_score}
            </div>
            """, unsafe_allow_html=True)
