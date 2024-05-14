import streamlit as st

def main():
    st.title("Square Button Interface")

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
        if st.button("Dark Souls"):
            st.session_state.page = "grid"
    with col4:
        if st.button("General Chat"):
            st.session_state.page = "grid"

def display_grid_page():
    back_col, _, _, _, _ = st.columns([1, 1, 1, 1, 1])
    with back_col:
        if st.button("Back to Home"):
            st.session_state.page = "home"

    # Top row with B I N G O
    cols = st.columns(5)
    bingo_letters = ['B', 'I', 'N', 'G', 'O']
    for j in range(5):
        cols[j].button(bingo_letters[j], key=f"bingo_letter_{j}")
    
    # 6x5 Grid of buttons
    for i in range(5):
        cols = st.columns(5)
        for j in range(5):
            cols[j].button("", key=f"grid_button_{i}_{j}")


if __name__ == "__main__":
    main()
