import streamlit as st
from Utils.dropdowns import *
from Logic.input_calculation import *

def batterieeinheit_form():
    st.subheader("Batterieeinheit")
    col1, col2 = st.columns(2)
    with col1:
        dynamischer_soc = st.selectbox("Dynamischer SOC an/aus", ANAUS_STATUS, index=0)
        use_case = st.selectbox("Use Case", BATTERY_USE_CASE_OPTIONS, index=0) 
        herstellername = st.selectbox("Hersteller Name", HERESTELLERNAME_OPTIONS, index=0)
        
        # Logic for changing value based on user's selction of herstellername 
        battery_values = {}
        speicherbezeichnung = ""
        is_disabled = True # Default to disabled unless "Freiteingabe" is selected

        if herstellername == HERESTELLERNAME_OPTIONS[1]:  # User select ecoCoach
            speicherbezeichnung = st.selectbox("Speicher Bezeichnung", SPEICHERBEZEICHNUNG_ECOCOACH_OPTIONS, key="ecoCoach_speicher")
            battery_values = ECOCOACH_VALUES.get(speicherbezeichnung, {})
            is_disabled = True  # Enable fields for ecoCoach selection

        elif herstellername == HERESTELLERNAME_OPTIONS[2]:  # User select adc_tec
            speicherbezeichnung = st.selectbox("Speicher Bezeichnung", SPEICHERBEZEICHNUNG_ADC_OPTIONS, key="adc_speicher")
            battery_values = ADC_VALUES.get(speicherbezeichnung, {})
            is_disabled = True
        else:
            speicherbezeichnung = st.text_input("Speicher Bezeichnung", value="nicht verfügbar wegen Freitexteingabe", disabled=True)
            battery_values = {}
            is_disabled = False  # Enable fields for Freitexteingabe
        
        # Value is dynamically changed based on user's seleciton of SpeicherBezeichnung
        ladeleistung = st.number_input("Ladeleistung [kW]", value=battery_values.get("ladeleistung", 0.0), disabled=is_disabled)
        kapazitätnutzbar = st.number_input("Kapazität nutzbar [kWh]", value=battery_values.get("kapazitaet_nutzbar", 0.0), disabled=is_disabled)
        ladenwirkungsgrad = st.number_input("Ladewirkungsgrad [%]", value=battery_values.get("wirkungsgrad", 0.0) * 100, disabled=is_disabled, format="%.1f")


    with col2:
        kaskade_lsk = st.number_input("Kaskade LSK", value=0)
        kaskade_evo = st.number_input("Kaskade EVO", value=0)
        gesamt_kaskade = kaskade_lsk + kaskade_evo
        st.number_input("Gesamte Kaskade", value=gesamt_kaskade, disabled=True)
        plausibilisierung = calculate_plausibilisierung_kaskade(herstellername, gesamt_kaskade)
        st.text_input("Plausibilisierung", value=plausibilisierung, disabled=True)

        # Value is dymically changed based on user's seleciton of SpeicherBezeichnung
        Kapazitätnominal = st.number_input("Kapazität nominal [kWh]", value=battery_values.get("kapazitaet_nominal", 0.0), disabled=bool(battery_values))
        Entladeleistung = st.number_input("Entladeleistung [kW]", value=battery_values.get("entladeleistung", 0.0), disabled=bool(battery_values))
        entladenwirkungsgrad = st.number_input("Entladenwirkungsgrad [%]", value=battery_values.get("wirkungsgrad", 0.0) * 100, disabled=bool(battery_values), format="%.1f")

        


    st.session_state.form_data["Batterieeinheit"] = {
        "Dynamischer_SOC": dynamischer_soc,
        "Use_Case": use_case,
        "Kaskade_LSK": kaskade_lsk,
        "Kaskade_EVO": kaskade_evo,
        "Gesamt_Kaskade": gesamt_kaskade,
        "Plausibilisierung": plausibilisierung,
        "Hersteller_Name": herstellername,
        "Speicher_Bezeichnung": speicherbezeichnung,
        "Ladeleistung": ladeleistung,
        "Kapazitaet_nutzbar": kapazitätnutzbar,
        "Ladenwirkungsgrad": ladenwirkungsgrad,
        "Kapazitaet_nominal": Kapazitätnominal,
        "Entladeleistung": Entladeleistung,
        "Entladenwirkungsgrad": entladenwirkungsgrad
    }
