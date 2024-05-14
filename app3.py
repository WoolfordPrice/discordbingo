import streamlit as st
import json
import random

def load_strings():
    with open('bingo_jsons_test.json', 'r') as f:
        data = json.load(f)
    return data["generic"]

def check_bingo(board_state, debug_messages):
    # Free space always counts towards bingo
    board_state[2][2] = True
    
    # Check rows
    for i in range(5):
        if all(board_state[i][j] for j in range(5)):
            debug_messages.append(f"Bingo on row {i + 1}")
            st.balloons()
            return True

    # Check columns
    for j in range(5):
        if all(board_state[i][j] for i in range(5)):
            debug_messages.append(f"Bingo on column {j + 1}")
            st.balloons()
            return True
    
    # Check diagonals
    if all(board_state[i][i] for i in range(5)):
        debug_messages.append("Bingo on main diagonal")
        st.balloons()
        return True
    if all(board_state[i][4 - i] for i in range(5)):
        debug_messages.append("Bingo on anti-diagonal")
        st.balloons()
        return True
    
    return False

def create_bingo_board(strings, debug_messages):
    # Add CSS styling for uniform button size
    st.markdown(
        """
        <style>
        .stButton > button {
            width: 125px;  /* Set a fixed width for all buttons */
            height: 125px;  /* Set a fixed height for all buttons */
            font-size: 16px;  /* Set the font size for the button text */
            margin: 10px;  /* Add margin to increase the distance between buttons */
        }
        .bingo-banner {
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }
        .bingo-column {
            flex: 1;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if "board_state" not in st.session_state:
        st.session_state.board_state = [[False for _ in range(5)] for _ in range(5)]
    
    if "strings" not in st.session_state:
        st.session_state.strings = load_strings()
        random.shuffle(st.session_state.strings)  # Shuffle strings to always get a new bingo board
    
    string_index = 0  # Establish index for shuffling

    # Display BINGO banner
    st.markdown('<div class="bingo-banner">' + ''.join([f'<div class="bingo-column">{letter}</div>' for letter in "BINGO"]) + '</div>', unsafe_allow_html=True)
    
    for row in range(5):
        cols = st.columns(5)
        for col in range(5):
            button_key = f"R{row + 1}C{col + 1}"
            
            if row == 2 and col == 2:
                button_label = "Free!"
            else:
                button_text = st.session_state.strings[string_index]
                button_label = "Clicked" if st.session_state.board_state[row][col] else button_text
                string_index += 1
                
            if cols[col].button(button_label, key=button_key):
                if not (row == 2 and col == 2):
                    st.session_state.board_state[row][col] = not st.session_state.board_state[row][col]
                if check_bingo(st.session_state.board_state, debug_messages):
                    st.balloons()
                    st.success('Bingo!')
                st.experimental_rerun()

def main():
    st.title("DISCORD BINGO")

    # Initialize debug messages
    if "debug_messages" not in st.session_state:
        st.session_state.debug_messages = []

    # Load strings from the JSON file
    strings = load_strings()
    
    # Create the bingo board
    create_bingo_board(strings, st.session_state.debug_messages)
    
    # Display debug messages
    st.subheader("Debug Messages")
    for message in st.session_state.debug_messages:
        st.text(message)

if __name__ == "__main__":
    main()

