import streamlit as st
import pandas as pd
from Logic.post_calculation import calculate_results
from Logic.validation import validate_form_data
from App_pages.input_sections.Batterieeinheit import batterieeinheit_form  
from App_pages.input_sections.Allgemeine_daten import allgemeine_daten_form
from App_pages.input_sections.pv_anlage import pv_anlage_form

# Start the form
def input_form():
    st.header("Kundendaten Eingabe")

    # Ensure form_data exists
    if "form_data" not in st.session_state:
        st.session_state.form_data = {}

    # Ensure Verbrauchsprofil is already provided (from upload_module)
    if "kundendaten_df" not in st.session_state:
        st.warning("Bitte geben Sie im Abschnitt 'Daten Upload' ein Verbrauchsprofil an.")
        return

    # Step 2: Define sub-pages
    sub_pages = ["Allgemeine Daten", "Batterieeinheit", "PV Anlage"]

    # Init session state for navigation
    if 'form_page_index' not in st.session_state:
        st.session_state.form_page_index = 0

    current_page = sub_pages[st.session_state.form_page_index]
    st.sidebar.markdown(f"**Aktueller Abschnitt:** {current_page}")

    # Show the correct form
    if current_page == "Allgemeine Daten":
        allgemeine_daten_form()
    elif current_page == "Batterieeinheit":
        batterieeinheit_form()
    elif current_page == "PV Anlage":
        pv_anlage_form()

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.form_page_index > 0:
            if st.button("← Zurück"):
                st.session_state.form_page_index -= 1
                st.rerun()
    with col2:
        if st.session_state.form_page_index < len(sub_pages) - 1:
            if st.button("Weiter →"):
                st.session_state.form_page_index += 1
                st.rerun()
        else:
            if st.button("Berechnen"):
                errors = validate_form_data(st.session_state.form_data)
                if errors:
                    st.warning("Bitte füllen Sie alle erforderlichen Felder aus.")
                    for error in errors:
                        st.error(error)
                    return
                results = calculate_results(st.session_state.form_data)
                st.session_state.results = results
                st.success("Berechnung abgeschlossen. Wechsle zur Ergebnisse-Seite.")
                st.rerun()
