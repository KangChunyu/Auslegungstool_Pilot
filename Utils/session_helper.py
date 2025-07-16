import streamlit as st

def get_uploaded_dataframes():
    kundendaten_df = st.session_state.get("kundendaten_df")
    pv_df = st.session_state.get("pv_df")
    dhbw_df = st.session_state.get("dhbw_df")
    return kundendaten_df, pv_df, dhbw_df
