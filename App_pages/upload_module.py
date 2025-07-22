import streamlit as st
import pandas as pd

def upload_files():
    st.header("Data Upload")
    
    kundendaten_file = st.file_uploader("Upload Kundendaten", type=['csv'])
    dhbw_file = st.file_uploader("Upload DHBW", type=['csv'])
    pv_file = st.file_uploader("Upload PV", type=['csv'])

    if kundendaten_file is not None:
        kundendaten_df = pd.read_csv(kundendaten_file)
        st.session_state.kundendaten_df = kundendaten_df
        st.success("Kundendaten file uploaded successfully!")
        st.dataframe(kundendaten_df.head())
        
    if dhbw_file is not None:
        dhbw_df = pd.read_csv(dhbw_file)
        st.session_state.dhbw_df = dhbw_df
        st.success("DHBW file uploaded successfully!")
        st.dataframe(dhbw_df.head())
        
    if pv_file is not None:
        pv_df = pd.read_csv(pv_file)
        st.session_state.pv_df = pv_df
        st.success("PV file uploaded successfully!")
        st.dataframe(pv_df.head())

    # Navigation Button logic
    if st.session_state.get("kunden_df") is not None or \
       st.session_state.get("dhbw_df") is not None or \
       st.session_state.get("pv_df") is not None:
        
        st.markdown("---")
        if st.button("Zur Eingabemaske →"):
            st.session_state.active_page = "Eingabe Form"
            st.rerun()  # refresh app and go to next page
