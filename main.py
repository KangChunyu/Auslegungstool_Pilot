import streamlit as st
from Pages.homepage import show_home
from Pages.upload_module import upload_files
from Pages.input_module import input_form
from Pages.results_module import display_results

def main():
    # Set page configuration first
    st.set_page_config(page_title="Bosch BESS Auslegungstool", layout="wide")

    # Inject custom styles early to hide default header/footer/sidebar
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stSidebarNav"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

    # Set custom app title
    st.title("Bosch BESS Auslegungstool :battery:")

    # Initialize session state for navigation
    if "active_page" not in st.session_state:
        st.session_state.active_page = "Home"

    # Sidebar navigation logic
    selected_page = st.sidebar.radio(
        "Seite auswählen",
        ["Home", "Data Upload", "Input Form", "Ergebnisse"],
        index=["Home", "Data Upload", "Input Form", "Ergebnisse"].index(st.session_state.active_page)
    )

    # Sync sidebar selection with session state
    if selected_page != st.session_state.active_page:
        st.session_state.active_page = selected_page

    # Page routing
    if st.session_state.active_page == "Home":
        show_home()
    elif st.session_state.active_page == "Data Upload":
        upload_files()
    elif st.session_state.active_page == "Input Form":
        input_form()
    elif st.session_state.active_page == "Ergebnisse":
        display_results()

if __name__ == "__main__":
    main()
