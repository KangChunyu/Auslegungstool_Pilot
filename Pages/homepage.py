import streamlit as st

def show_home():
    st.title("Willkommen beim Bosch BESS Auslegungstool!!")

    st.markdown("""
    Dieses Tool unterstützt Sie bei der Auslegung und Analyse von Batteriespeichersystemen.  
    Nutzen Sie die Seitenleiste, um mit dem Hochladen Ihrer Daten zu beginnen oder Eingaben vorzunehmen.

    **Ablauf:**
    1. Daten hochladen (Kundendaten, DHBW, PV)
    2. Eingabemaske ausfüllen
    3. Ergebnisse anzeigen
    """)
