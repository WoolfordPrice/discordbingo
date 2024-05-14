import streamlit as st
import json
import random

def load_strings():
    with open('bingo_jsons_test.json', 'r') as f:
        data = json.load(f)
    return data["generic"]


def check_bingo(board_state):
    #check rows and columns
    for i in range(5):
        if all(board_state[i][j] for j in range(5)):
            return True
        if all (board_state[j][i] for j in range(5)):
            return True
        
    #check diagonals
    if all(board_state[i][i] for i in range(5)):
        return True
    if all(board_state[i][4-i] for i in range(5)):
        return True
    
    return False

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
        
    if "strings" not in st.session_state:
        st.session_state.strings = load_strings()
        random.shuffle(st.session_state.strings) #shuffle the strings to always get a new bingo board
        
    string_index = 0 #establish index for shuffling
        
    cols = st.columns(5)
    bingo_letters = ["B", "I", "N", "G", "O"]
    for i, letter in enumerate(bingo_letters):
        cols[i].button(letter, key=f"BINGO_{letter}")
    
    for row in range(5):
        cols = st.columns(5)
        for col in range(5):
            button_key = f"R{row+1}C{col+1}"
            
            if row == 2 and col == 2:
                button_label = "Free!"
            else:
                button_text = st.session_state.strings[string_index]
                button_label = "Clicked" if st.session_state.board_state[row][col] else button_text
                string_index += 1
                
            if cols[col].button(button_label, key=button_key):
                if not (row == 2 and col == 2):
                    st.session_state.board_state[row][col] = not st.session_state.board_state[row][col]
                st.experimental_rerun()
                if check_bingo(st.session_state.board_state):
                    st.balloons()
                    st.success('Bingo!')
                st.experiemental_rerun()

def main():
    st.title("DISCORD BINGO")

    #load strings from the json file
    strings = load_strings()
    
    # Create the bingo board
    create_bingo_board(strings)

if __name__ == "__main__":
    main()
