import streamlit as st
import json
import random

def load_strings():
    with open('bingo_jsons_test.json', 'r') as f:
        data = json.load(f)
    return data["generic"]

def create_bingo_board(strings):
    # Add CSS styling for uniform button size
    st.markdown(
        """
        <style>
        .stButton > button {
            width: 125px;  /* Set a fixed width for all buttons */
            height: 125px;  /* Set a fixed height for all buttons */
            font-size: 16px; /* Set the font size for the button text */
            margin: 10px, 50px;  /* Add margin to increase the distance between buttons */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if "board_state" not in st.session_state:
        st.session_state.board_state = [[False for _ in range(5)] for _ in range(5)]
        st.session_state.strings = strings
        random.shuffle(st.session_state.strings) #shuffle the strings to always get a new bingo board

    cols = st.columns(5)
    bingo_letters = ["B", "I", "N", "G", "O"]
    for i, letter in enumerate(bingo_letters):
        cols[i].button(letter, key=f"BINGO_{letter}")
    
    for row in range(5):
        cols = st.columns(5)
        for col in range(5):
            button_key = f"R{row+1}C{col+1}"
            button_text = st.session_state.strings[string_index] #get a unique string
            button_label = button_text
            string_index += 1

            if cols[col].button(button_label, key=button_key):
                st.session_state.board_state[row][col] = not st.session_state.board_state[row][col]
                st.experimental_rerun()

def main():
    st.title("DISCORD BINGO")

    #load strings from the json file
    strings = load_strings()
    
    # Create the bingo board
    create_bingo_board(strings)

if __name__ == "__main__":
    main()