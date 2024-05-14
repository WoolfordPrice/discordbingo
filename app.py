import streamlit as st

def main():
    st.title("""
     ________    _______________
    |   ___  \\  /              /
    |  |   \\  |/              /\\
    |  |   |  |__  ___     __/ _\\____   ______
    |  |__/  /|  |/   \\   |  |/  ____\\ /  __  \\
    |   __  < |  |     \\  |  |  |     |  |  |  |
    |  |  \\  \\|  |  |\\  \\ |  |  |  ___|  |  |  |
    |  |   |  |  |  | \\  \\|  |  | /_  |  |  |  |
    |  |___/  |  |  |  \\     |  |__/  |  |__|  |
    |________/|__|\\_|  /\\___/ \\______/\\\\______/
      /               /\\               \\
     /______GAME_____/OF\\____NUMBERS____\\
""")

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        display_home_page()
    elif st.session_state.page == "grid":
        display_grid_page()

def display_home_page():
    st.markdown("<style>.container { display: flex; justify-content: center; }</style>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Arena"):
            st.session_state.page = "grid"
    with col2:
        if st.button("TFT"):
            st.session_state.page = "grid"
    col3, col4 = st.columns([1, 1])
    with col3:
        if st.button("Souls-Like"):
            st.session_state.page = "grid"
    with col4:
        if st.button("General Chat"):
            st.session_state.page = "grid"

def display_grid_page():
    # CSS for styling the buttons
    st.markdown("""
        <style>
        .square-button {
            width: 80px;
            height: 80px;
            display: inline-block;
            text-align: center;
            vertical-align: middle;
            line-height: 76px;
            margin: 5px;
            border: 2px solid black;
            background-color: #f0f0f0;
        }
        .square-button.pressed {
            background-color: blue !important;
            color: white !important;
            border: 2px solid white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    back_col, _, _, _, _ = st.columns([1, 1, 1, 1, 1])
    with back_col:
        if st.button("Back to Home"):
            st.session_state.page = "home"

    # Top row with B I N G O
    cols = st.columns(5)
    bingo_letters = ['B', 'I', 'N', 'G', 'O']
    for j in range(5):
        cols[j].button(bingo_letters[j], key=f"bingo_letter_{j}")

    # Initialize session state for buttons if not already done
    if "pressed_buttons" not in st.session_state:
        st.session_state.pressed_buttons = [[False for _ in range(5)] for _ in range(6)]

    # 6x5 Grid of buttons
    for i in range(1, 6):  # Start from 1 to skip the BINGO row
        cols = st.columns(5)
        for j in range(5):
            button_key = f"grid_button_{i}_{j}"
            if st.button(" ", key=button_key):
                st.session_state.pressed_buttons[i][j] = not st.session_state.pressed_buttons[i][j]
            
            button_class = "square-button pressed" if st.session_state.pressed_buttons[i][j] else "square-button"
            st.markdown(f'<button class="{button_class}"> </button>', unsafe_allow_html=True)



if __name__ == "__main__":
    main()
