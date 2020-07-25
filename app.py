import streamlit as st
import src.pages.home
import src.pages.dashboard
import src.pages.forecaster
import src.pages.about


PAGES = {
    "Home": src.pages.home,
    "Dashboard": src.pages.dashboard,
    "Forecaster": src.pages.forecaster,
    "About": src.pages.about
}


def main():
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
    PAGES[choice].main()


if __name__ == "__main__":
    main()
