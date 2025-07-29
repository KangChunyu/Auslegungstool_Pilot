import streamlit as st
from Logic.input_calculation import *
from Utils.dropdowns import *

def allgemeine_daten_form():
    st.subheader("Projekt Information")
    col1, col2 = st.columns(2)
    with col1:
        projektname = st.text_input("Projektname")
        projektversion = st.text_input("Projektversion")
        datum = st.date_input("Datum")
        datum_preisversenden = st.date_input("Datum Preisversenden")
    with col2:
        kundenname = st.text_input("Kundenname")
        kundendaten_type = st.selectbox("Kundendaten Type", KUNDENDATEN_OPTIONS, index=0, key="kundendaten_type")
        kundendaten_status = st.selectbox("Kundendaten Status", ANAUS_STATUS, index=0, key="kundendaten_status")

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
        # Calculate Jahresbenutzungsdauer based on input values
        jahresbenutzungsdauer = calculate_jahresbenutzungsdauer(energieverbrauch, max_jahresleistung)
        st.number_input(f"Jahresbenutzungsdauer [h]", value=jahresbenutzungsdauer, disabled=True)

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
        hystereseleistung = st.number_input("Hystereseleistung [kVA]")
    with col2:
        vereinbarte_anschlussleistung = st.number_input("vereinbarte Anschlussleistung [kVA]")
        installierte_ausschusleistung = st.number_input("Installierte Ausschusleistung [kVA]")
        

    st.session_state.form_data["Netzentgelt"] = {
        "Max_Anschlussleistung": max_anschlussleistung,
        "Vereinbarte_Anschlussleistung": vereinbarte_anschlussleistung,
        "Hystereseleistung": hystereseleistung,
        "Installierte_Ausschusleistung": installierte_ausschusleistung
    }
