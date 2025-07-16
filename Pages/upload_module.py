import streamlit as st
import pandas as pd

def upload_files():
    st.header("Data Upload")
    
    kundendaten_file = st.file_uploader("Upload Kundendaten", type=['csv'])
    dhbw_file = st.file_uploader("Upload DHBW", type=['csv'])
    pv_file = st.file_uploader("Upload PV", type=['csv'])

    if kundendaten_file is not None:
        st.session_state.kundendaten_df = pd.read_csv(kundendaten_file)
        st.success("Kundendaten file uploaded successfully!")
        
    if dhbw_file is not None:
        st.session_state.dhbw_df = pd.read_csv(dhbw_file)
        st.success("DHBW file uploaded successfully!")
        
    if pv_file is not None:
        st.session_state.pv_df = pd.read_csv(pv_file)
        st.success("PV file uploaded successfully!")

    # Navigation Button logic
    if st.session_state.get("kundendaten_df") is not None or \
       st.session_state.get("dhbw_df") is not None or \
       st.session_state.get("pv_df") is not None:
        
        st.markdown("---")
        if st.button("Zur Eingabemaske →"):
            st.session_state.active_page = "Input Form"
            st.rerun()  # ✅ Fixes the double-click issue
