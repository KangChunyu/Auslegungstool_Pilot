def calculate_results(input_data, kundendaten_df=None, pv_df=None):
    results = {}

    # Project Info
    info = input_data.get("Project Information", {})
    results["Project Information"] = {
        "Project Name": info.get("Projektname", ""),
        "Customer": info.get("Kundenname", ""),
        "Date": info.get("Datum", "")
    }

    # Energy
    energy = input_data.get("Energiebezugsdaten", {})
    try:
        annual_kwh = float(energy.get("Energieverbrauch", 0))
        price_per_kwh = float(energy.get("Brutto_Stromkosten_kWh", 0))
        total_cost = annual_kwh * price_per_kwh
    except:
        annual_kwh = price_per_kwh = total_cost = 0

    results["Energy Analysis"] = {
        "Energieverbrauch": f"{annual_kwh:,.2f} kWh",
        "Stromkosten[€/kWh]": f"€{price_per_kwh:.4f}",
        "Jährliche Gesamtkosten": f"€{total_cost:,.2f}"
    }

    # Kundendaten
    if kundendaten_df is not None and 'Verbrauch [kWh]' in kundendaten_df.columns:
        results["Kundendaten Analyse"] = {
            "Summe Verbrauch aus Kundendaten": f"{kundendaten_df['Verbrauch [kWh]'].sum():,.2f} kWh"
        }

    # PV
    if pv_df is not None and 'PV-Produktion' in pv_df.columns:
        results.setdefault("PV Analyse", {})["Durchschnittliche PV-Produktion"] = f"{pv_df['PV-Produktion'].mean():,.2f} kWh"

    return results
