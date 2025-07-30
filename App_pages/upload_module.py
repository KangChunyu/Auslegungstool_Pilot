import streamlit as st
import pandas as pd
from Utils.data_loader import load_standard_profile

# function to detect the time interval of the timestamp column
def detect_time_interval(df):
    if "timestamp" not in df.columns or df.shape[0] < 2:
        return "Unbekannt"
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    valid_ts = df["timestamp"].dropna()
    if len(valid_ts) < 2:
        return "Ungültiges Zeitformat"
    delta = valid_ts.diff().dropna().mode()[0]
    return delta

# function to change time unit from 1 hour to 15 minutes
def normalize_to_15min(df):
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df = df.set_index("timestamp").sort_index()
    interval = detect_time_interval(df)
    if interval == pd.Timedelta("1H"):
        df = df.resample("15T").interpolate(method="linear")
    return df.reset_index()

# function manage the upload of files and selection of standard profiles
def upload_files():
    st.header("Daten hochladen")

    if "form_data" not in st.session_state:
        st.session_state.form_data = {}

    st.subheader("Eignendaten hochladen / Stadardlastprofil auswählen")

    if "standard_profiles" not in st.session_state:
        try:
            st.session_state.standard_profiles = load_standard_profile()
        except Exception as e:
            st.warning(f"Standardprofile konnten nicht geladen werden: {e}")
            st.session_state.standard_profiles = {}

    if "profil_option" not in st.session_state:
        st.session_state.profil_option = "Standardlastprofil auswählen"

    st.session_state.profil_option = st.radio(
        "Wie möchten Sie das Verbrauchsprofil angeben?",
        ["Eigene Datei hochladen", "Standardlastprofil auswählen"],
        index=0
    )

    profil_loaded = False

    if st.session_state.profil_option == "Eigene Datei hochladen":
        uploaded_file = st.file_uploader("CSV-Datei für Verbrauchsprofil hochladen", type=["csv"], key="verbrauchsprofil_upload")
        
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            if "timestamp" not in df.columns:
                df.rename(columns={df.columns[0]: "timestamp"}, inplace=True)

            df = normalize_to_15min(df)
            interval = detect_time_interval(df)

            st.info(f"Erkannte Zeitauflösung nach Umrechnung: **{interval}**")
            st.session_state.kundendaten_df = df
            st.success("Verbrauchsprofil erfolgreich verarbeitet und als Kundendaten gespeichert.")
            st.dataframe(df.head())
            profil_loaded = True
        else:
            st.info("Bitte laden Sie eine Verbrauchsprofil-Datei hoch.")

    else:
        if st.session_state.standard_profiles:
            selected_profile = st.selectbox(
                "Wählen Sie ein Standardlastprofil",
                list(st.session_state.standard_profiles.keys()),
                key="standardprofil_auswahl"
            )
            preview_df = st.session_state.standard_profiles[selected_profile]
            interval = detect_time_interval(preview_df)
            st.info(f"Profilauflösung: **{interval}**")

            st.session_state.kundendaten_df = preview_df
            st.session_state["selected_lastprofil_name"] = selected_profile
            st.success(f"Standardprofil '{selected_profile}' ausgewählt.")
            st.dataframe(preview_df.head())
            profil_loaded = True
        else:
            st.warning("Keine Standardprofile gefunden.")

    st.markdown("---")


    # Section 2: Upload DHBW and PV files into the system
    dhbw_file = st.file_uploader("DHBW hochladen", type=['csv'])
    pv_file = st.file_uploader("PV hochladen", type=['csv'])

    if dhbw_file is not None:
        dhbw_df = pd.read_csv(dhbw_file)
        if "timestamp" not in dhbw_df.columns:
            dhbw_df.rename(columns={dhbw_df.columns[0]: "timestamp"}, inplace=True)
        dhbw_df = normalize_to_15min(dhbw_df)
        st.session_state.dhbw_df = dhbw_df
        st.success("DHBW-Datei erfolgreich hochgeladen und normalisiert!")
        st.dataframe(dhbw_df.head())

    if pv_file is not None:
        pv_df = pd.read_csv(pv_file)
        if "timestamp" not in pv_df.columns:
            pv_df.rename(columns={pv_df.columns[0]: "timestamp"}, inplace=True)
        pv_df = normalize_to_15min(pv_df)
        st.session_state.pv_df = pv_df
        st.success("PV-Datei erfolgreich hochgeladen und normalisiert!")
        st.dataframe(pv_df.head())

    st.markdown("---")

    if st.button("Zur Eingabemaske →"):
        if "kundendaten_df" not in st.session_state:
            st.warning("Bitte wählen oder laden Sie ein Verbrauchsprofil (Kundendaten).")
        else:
            st.session_state.active_page = "Eingabe Form"
            st.rerun()
