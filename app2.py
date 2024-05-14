import streamlit as st

def create_bingo_board():
    # Add CSS styling for uniform button size
    st.markdown(
        """
        <style>
        .stButton > button {
            width: 100px;  /* Set a fixed width for all buttons */
            height: 100px;  /* Set a fixed height for all buttons */
            font-size: 16px; /* Set the font size for the button text */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if "board_state" not in st.session_state:
        st.session_state.board_state = [[False for _ in range(5)] for _ in range(5)]

    cols = st.columns(5)
    bingo_letters = ["B", "I", "N", "G", "O"]
    for i, letter in enumerate(bingo_letters):
        cols[i].button(letter, key=f"BINGO_{letter}")
    
    for row in range(5):
        cols = st.columns(5)
        for col in range(5):
            button_key = f"R{row+1}C{col+1}"
            button_label = "Clicked" if st.session_state.board_state[row][col] else button_key

            if cols[col].button(button_label, key=button_key):
                st.session_state.board_state[row][col] = not st.session_state.board_state[row][col]
                st.experimental_rerun()

def main():
    st.title("Interactive Bingo Board")

    # Create the bingo board
    create_bingo_board()

if __name__ == "__main__":
    main()
