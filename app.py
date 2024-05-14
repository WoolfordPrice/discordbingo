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
        if st.button("Square 1"):
            st.session_state.page = "grid"
    with col2:
        if st.button("Square 2"):
            st.session_state.page = "grid"
    col3, col4 = st.columns([1, 1])
    with col3:
        if st.button("Square 3"):
            st.session_state.page = "grid"
    with col4:
        if st.button("Square 4"):
            st.session_state.page = "grid"

def display_grid_page():
    back_col, _, _, _, _ = st.columns([1, 1, 1, 1, 1])
    with back_col:
        if st.button("Back to Home"):
            st.session_state.page = "home"
    
    for i in range(5):
        cols = st.columns(5)
        for j in range(5):
            cols[j].button("")

if __name__ == "__main__":
    main()
