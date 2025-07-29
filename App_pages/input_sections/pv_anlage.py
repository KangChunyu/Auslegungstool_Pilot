import streamlit as st
from Utils.dropdowns import *

def pv_anlage_form():
    st.subheader("PV Anlage - Technische Daten")

    col1, col2 = st.columns(2)

    with col1:
        nennleistung = st.number_input("Nennleistung [kWp]", min_value=0.0, value=0.0)
        ertragsprofil = st.selectbox("Ertragsprofil", ERTRAGSPROFIL_OPTIONS, index=0)
        ausrichtung1 = st.number_input("Anteil PV-Fläche Ausrichtung 1 [%]", min_value=0.0, max_value=100.0, value=100.0)

        # Automatically calculate Ausrichtung 2
        ausrichtung2 = max(0.0, min(100.0, 100.0 - ausrichtung1)) # clamp between 0 and 100
        st.number_input("Anteil PV-Fläche Ausrichtung 2 [%]", min_value=0.0, max_value=100.0, value=ausrichtung2, disabled=True)  
        status = "KORREKT" if ausrichtung1 + ausrichtung2 == 100.0 else "NICHT KORREKT"

    with col2:
        st.text_input("Nennleistung [kWp] (2)", value="Nicht bearbeitbar", disabled=True)
        st.selectbox("Ertragsprofil (2)", ["Nicht bearbeitbar"], disabled=True)
        st.text_input("Status der Eingabe (2)", value=status, disabled=True)

    # Store values in session state
    st.session_state.form_data["PV Anlage"] = {
        "Nennleistung_kWp": nennleistung,
        "Ertragsprofil": ertragsprofil,
        "Anteil_Ausrichtung_1": ausrichtung1,
        "Anteil_Ausrichtung_2": ausrichtung2,
        "Status": status
    }
