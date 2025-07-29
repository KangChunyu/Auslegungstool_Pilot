import streamlit as st

# Set page configuration first
st.set_page_config(page_title="Bosch BESS Tool", layout="wide")


from App_pages.homepage import show_home
from App_pages.upload_module import upload_files
from App_pages.input_module import input_form
from App_pages.results_module import display_results

def main():

    # Set custom app title and logo
    col1, col2 = st.columns([1,8]) # Logo and text in 1:8 ratio
    with col1:
        st.image("Assets/BuderusLogo.png", width=100) #sert logo in the home page
    with col2:
        st.title("Buderus Auslegungstool :battery:")

    # Initialize session state for navigation
    if "active_page" not in st.session_state:
        st.session_state.active_page = "Home"

    # Sidebar content
    with st.sidebar:
        st.header("Navigation")
        st.markdown("Wählen Sie eine Seite aus dem Menü aus, um fortzufahren.")

    # Sidebar navigation logic implementation
    pages = ["Home", "Daten Upload", "Eingabe Form", "Ergebnisse"]
    selected_page = st.sidebar.radio(
        "Seite auswählen",
        pages,
        index=pages.index(st.session_state.active_page)
    )

    # Sync user sidebar selection with session state
    if selected_page != st.session_state.active_page:
        st.session_state.active_page = selected_page

        # Default first subpage when user click on the "Eingabe Form" page
        if st.session_state.active_page == "Eingabe Form":
            st.session_state.form_page_index = 0
        st.rerun()

    # Show all subpages under Eingabe Form
    if st.session_state.active_page == "Eingabe Form":
        
        # Define sub-pages for the input form
        sub_pages = ["Allgemeine Daten", "Batterieeinheit", "PV Anlage"]
    
        # Make sure sub page index is 0
        if 'form_page_index' not in st.session_state:
            st.session_state.form_page_index = 0 

        # Show Subpage radio menu in the sidebar
        selected_sub_page = st.sidebar.radio(
            "Abschnitt auswählen",
            sub_pages,
            index=st.session_state.form_page_index
        )

        # Update sub-page state
        if selected_sub_page != sub_pages[st.session_state.form_page_index]:
            st.session_state.form_page_index = sub_pages.index(selected_sub_page)
            st.rerun()


    # Page routing
    if st.session_state.active_page == "Home":
        show_home()
    elif st.session_state.active_page == "Daten Upload":
        upload_files()
    elif st.session_state.active_page == "Eingabe Form":
        input_form()
    elif st.session_state.active_page == "Ergebnisse":
        display_results()

if __name__ == "__main__":
    main()
