import streamlit as st
import pandas as pd
from Core.calculation import calculate_results
from Core.validation import validate_form_data
from Utils.session_helper import get_uploaded_dataframes

def display_results():
    st.header("🔁 Ergebnisse und Letzte Änderungen")

    if 'form_data' not in st.session_state:
        st.info("Noch keine Eingabedaten vorhanden. Bitte zuerst das Formular ausfüllen.")
        return

    form_data = st.session_state.form_data
    edited_form_data = {}

    st.markdown("### ✏️ Eingabedaten anpassen")

    # Loop through sections and fields for editing
    for section, fields in form_data.items():
        st.subheader(section)
        edited_form_data[section] = {}

        for key, value in fields.items():
            try:
                if isinstance(value, (int, float)):
                    new_value = st.number_input(f"{section} - {key}", value=value, key=f"{section}-{key}")
                elif isinstance(value, pd.Timestamp):
                    new_value = st.date_input(f"{section} - {key}", value=value, key=f"{section}-{key}")
                else:
                    new_value = st.text_input(f"{section} - {key}", value=str(value), key=f"{section}-{key}")
                edited_form_data[section][key] = new_value

            except Exception as e:
                st.error(f"Fehler beim Bearbeiten von {section}: {e}")

    # Recalculate button
    if st.button("🔁 Nochmal berechnen"):
        try:
            kundendaten_df, pv_df, _ = get_uploaded_dataframes()

            # Merge edited values into the full form_data
            for section in edited_form_data:
                st.session_state.form_data[section].update(edited_form_data[section])

            # Validate updated form data
            validation_errors = validate_form_data(st.session_state.form_data)
            if validation_errors:
                for err in validation_errors:
                    st.error(err)
                st.stop()

            # Recalculate results
            st.session_state.results = calculate_results(st.session_state.form_data, kundendaten_df, pv_df)
            st.success("Erneute Berechnung erfolgreich!")

            # ✅ Immediate rerun so the results appear without second click
            st.rerun()

        except Exception as e:
            st.error(f"Fehler bei der Berechnung: {e}")
            return

    # Show original inputted values (optional: skip Projekt Information)
    st.markdown("### 📥 Ursprüngliche Eingabedaten")
    for section, fields in st.session_state.form_data.items():
        if section == "Projekt Information":  # ❌ remove if you want to hide it
            continue
        st.subheader(section)
        input_table = pd.DataFrame({
            "Feld": list(fields.keys()),
            "Wert": list(fields.values())
        })
        st.table(input_table)

    # Show results if available
    if 'results' in st.session_state:
        st.markdown("### 📊 Ergebnisse")
        results = st.session_state.results
        for section_name, section_data in results.items():
            st.subheader(section_name)
            for key, value in section_data.items():
                st.write(f"**{key}**: {value}")

        # Export results button
        if st.button("📥 Ergebnisse Exportieren"):
            flat_results = {}
            for section, data in results.items():
                for key, value in data.items():
                    flat_results[f"{section} - {key}"] = value

            df = pd.DataFrame([flat_results])
            st.download_button(
                label="Download CSV",
                data=df.to_csv(index=False),
                file_name="results.csv",
                mime="text/csv"
            )
    else:
        st.info("Noch keine Ergebnisse verfügbar. Bitte zuerst berechnen.")
