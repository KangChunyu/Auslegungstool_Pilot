import streamlit as st
from Logic.calculation import calculate_results
from Logic.validation import validate_form_data  # make sure to import this if in separate file

def input_form():
    st.header("Kundendaten Eingabe")

    # Define sub-pages for the input form
    sub_pages = ["Allgemeine Daten", "Batterieeinheit"] 

    kundendaten_options = [
        "volatile Erzeugung 1", "volatile Erzeugung 2", 
        "volatile Erzeugung 3", "volatile Erzeugung 4",
        "steurbare Erzeugung 1", "steurbare Erzeugung 2", 
        "steurbare Erzeugung 3", "steurbare Erzeugung 4", 
        "Netzbezug"
    ]

    if 'form_page_index' not in st.session_state:
        st.session_state.form_page_index = 0
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    # Set default kundendaten_type to first one  
    if 'kundendaten_type' not in st.session_state:
        st.session_state.kundendaten_type = kundendaten_options[0]

    # Cursor to show current subpage
    current_page = sub_pages[st.session_state.form_page_index]
    st.sidebar.markdown(f"**Aktueller Abschnitt:** {current_page}")

    if current_page == "Allgemeine Daten":
        st.subheader("Projekt Information")
        col1, col2 = st.columns(2)
        with col1:
            projektname = st.text_input("Projektname")
            projektversion = st.text_input("Projektversion")
            datum = st.date_input("Datum")
            datum_preisversenden = st.date_input("Datum Preisversenden")
        with col2:
            kundenname = st.text_input("Kundenname")
            kundendaten_type = st.selectbox("Kundendaten Type", options=kundendaten_options, key="kundendaten_type")
            kundendaten_status = st.selectbox("Kundendaten Status", ["An", "Aus"])

        st.session_state.form_data["Projekt Information"] = {
            "Projektname": projektname,
            "Projektversion": projektversion,
            "Kundenname": kundenname,
            "Datum": datum,
            "Datum_Preisversenden": datum_preisversenden,
            "Kundendaten_Type": kundendaten_type,
            "Kundendaten_Status": kundendaten_status
        }

        st.subheader("Energiebezugsdaten")
        col1, col2 = st.columns(2)
        with col1:
            gewaehltes_profil = st.text_input("Gewähltes Profil", value=st.session_state.kundendaten_type, disabled=True)
            brutto_stromkosten = st.number_input("Brutto Stromkosten")
            energieverbrauch = st.number_input("Energieverbrauch p.a. [kWh]")
        with col2:
            brutto_stromkosten_kwh = st.number_input("Brutto Stromkosten [€/kWh]")
            max_jahresleistung = st.number_input("max. Jahresleistung, Lastprofil [kW]", value=0.00)
            jahresbenutzungsdauer = (
                round(energieverbrauch / max_jahresleistung, 2)
                if energieverbrauch > 0 and max_jahresleistung > 0
                else 0.00
            )
            st.text(f"Jahresbenutzungsdauer [h]: {jahresbenutzungsdauer}")

        st.session_state.form_data["Energiebezugsdaten"] = {
            "Gewähltes_Profil": gewaehltes_profil,
            "Brutto_Stromkosten": brutto_stromkosten,
            "Energieverbrauch": energieverbrauch,
            "Brutto_Stromkosten_kWh": brutto_stromkosten_kwh,
            "Max_Jahresleistung": max_jahresleistung,
            "Jahresbenutzungsdauer": jahresbenutzungsdauer
        }

        st.subheader("Netzentgelt Netzbetreiber")
        col1, col2 = st.columns(2)
        with col1:
            max_anschlussleistung = st.number_input("Maximale Anschlussleistung [kVA]")
        with col2:
            vereinbarte_anschlussleistung = st.number_input("vereinbarte Anschlussleistung [kVA]")
            gewaehltes_lastprofil = st.text_input("Gewähltes Lastprofil")

        st.session_state.form_data["Netzentgelt"] = {
            "Max_Anschlussleistung": max_anschlussleistung,
            "Vereinbarte_Anschlussleistung": vereinbarte_anschlussleistung,
            "Gewähltes_Lastprofil": gewaehltes_lastprofil
        }

    elif current_page == "Batterieeinheit":
        st.subheader("Batterieeinheit")
        col1, col2 = st.columns(2)
        with col1:
            dynamischer_soc = st.selectbox("Dynamischer SOC an/aus", ["An", "Aus"])
            use_case = st.selectbox("Use-Case", ["Eigenverbrauch", "Netzstabilisierung", "Notstromversorgung"])
        with col2:
            kaskade_lsk = st.text_input("Kaskade LSK")
            kaskade_evo = st.text_input("Kaskade EVO")

        st.session_state.form_data["Batterieeinheit"] = {
            "Dynamischer_SOC": dynamischer_soc,
            "Use_Case": use_case,
            "Kaskade_LSK": kaskade_lsk,
            "Kaskade_EVO": kaskade_evo
        }

    # Navigation buttons with rerun fix
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
