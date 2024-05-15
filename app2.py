import streamlit as st
import json
import random

# Function to switch pages
def set_page(page, board_type=None):
    st.session_state.current_page = page
    if board_type:
        st.session_state.board_type = board_type
        
    # Set displa yname for each board type
    board_names = {
        "league": "League",
        "arena": "Arena",
        "tft": "TFT",
        "soulsLike": "Souls Like"
    }
    st.session_state.board_name = board_names.get(board_type, "Discord")

# Function to load strings from JSON
def load_strings(board_type):
    with open('bingos_spots.json', 'r') as f:
        data = json.load(f)
        
    #accessing different board types
    specific_list  = data["exclusive"].get(board_type, [])
    generic_list = data.get("generic",[])
    
    combined_list = specific_list + generic_list
    random.shuffle(combined_list)
    return combined_list

# Function to check bingo conditions
def check_bingo(board_state):
    board_state[2][2] = True  # Free space always counts towards bingo

    # Check rows
    for i in range(5):
        if all(board_state[i][j] for j in range(5)):
            return True

    # Check columns
    for j in range(5):
        if all(board_state[i][j] for i in range(5)):
            return True

    # Check diagonals
    if all(board_state[i][i] for i in range(5)):
        return True
    if all(board_state[i][4 - i] for i in range(5)):
        return True

    return False

# Function to create bingo board
def create_bingo_board():
    st.markdown(
        """
        <style>
        .stButton > button {
            width: 125px;
            height: 125px;
            font-size: 16px;
            margin: 10px;
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
        .banner-red {
            color: red;
        }
        .banner-white {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    #initialize a board with no squares clicked
    if "board_state" not in st.session_state:
        st.session_state.board_state = [[False for _ in range(5)] for _ in range(5)]

    #populate board type
    board_type = st.session_state.get("board_type", "generic")
    if "strings" not in st.session_state:
        st.session_state.strings = load_strings(board_type)
        st.session_state.board_type = board_type
        

    if "bingo" not in st.session_state:
        st.session_state.bingo = False

    string_index = 0
    banner_class = "banner-red" if st.session_state.bingo else "banner-white"

    st.markdown('<div class="bingo-banner ' + banner_class + '">' + ''.join([f'<div class="bingo-column">{letter}</div>' for letter in "BINGO"]) + '</div>', unsafe_allow_html=True)

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

                st.session_state.bingo = False
                if check_bingo(st.session_state.board_state):
                    st.success('Bingo!')
                    st.session_state.bingo = True
                st.experimental_rerun()

    st.button("Back to Home", on_click=lambda: set_page("home"))
    

# Function to display the home page
def home_page():
    st.markdown(
        """
        <style>
        .home-button {
            display: inline-block;
            width: 200px;
            height: 200px;
            font-size: 20px;
            margin: 20px;
            line-height: 180px; /* Center text vertically */
            text-align: center; /* Center text horizontally */
            background-color: #007BFF; /* Button color */
            color: white;
            border-radius: 10px;
            cursor: pointer;
        }
        .home-button:hover {
            background-color: #0056b3; /* Darker shade on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(2)
    if cols[0].button("League", key="league_btn", on_click=lambda: set_page("bingo", "league")):
        pass
    if cols[1].button("TFT", key="tft_btn", on_click=lambda: set_page("bingo", "tft")):
        pass
    cols = st.columns(2)
    if cols[0].button("Souls Like", key="souls_btn", on_click=lambda: set_page("bingo", "soulsLike")):
        pass
    if cols[1].button("Arena", key="arena_btn", on_click=lambda: set_page("bingo", "arena")):
        pass

# Main function to control page navigation
def main():
    board_name = st.session_state.get("board_name", "Discord")
    st.title(f"{board_name} Bingo")

    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"

    if "bingo" not in st.session_state:
        st.session_state.bingo = False

    # Initialize bingo message state
    if "bingo_message" not in st.session_state:
        st.session_state.bingo_message = False

    # Page navigation
    if st.session_state.current_page == "home":
        home_page()
    elif st.session_state.current_page == "bingo":
        create_bingo_board()

    # Display bingo message
    if st.session_state.bingo_message:
        st.success('Bingo!')

if __name__ == "__main__":
    main()
