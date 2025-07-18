import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

def initialize_fields():
    # Define a dictionary to store field names and their corresponding variables
    fields = {
        "Projektname": tk.StringVar(),
        "Projektversion": tk.StringVar(),
        "Kundenname": tk.StringVar(),
        "Datum": tk.StringVar(),
        "Datum_Preisversenden": tk.StringVar(),
        
        # Energiebezugsdaten 
        "Header_Energiebezugsdaten": tk.StringVar(),
        "Gewähltes_Profil": tk.StringVar(),
        "Brutto_Stromkosten": tk.StringVar(),
        "Energieverbrauch p.a. [kWh]": tk.StringVar(),
        "Brutto Stromkosten [€/kWh]": tk.StringVar(),
        "max. Jahresleistung, Lastprofil [kW]": tk.StringVar(),
        "Jahresbenutzungsdauer [h]" : tk.StringVar(),    

        # Netzenentgelt 
        "Header_Netzentgelt Netzbetreiber": tk.StringVar(),
        "Maximale Anschlussleistung [kVA]": tk.StringVar(),
        "vereinbarte Anschlussleistung [kVA]": tk.StringVar(),
        "Gewähltes Lastprofil": tk.StringVar(),
        

        # Add dropdown fields
        "Kundendaten_Type": tk.StringVar(),
        "Kundendaten_Status": tk.StringVar(),
    }

    # Define the field for showing fixed value
    predefined_fields = {
        "Energieverbrauch p.a. [kWh]": "Fehler",
        "max. Jahresleistung, Lastprofil [kW]": "0.00",
        "Jahresbenutzungsdauer [h]": cal_jahresbenutzungsdauer(fields),
    }

    # Define Dropdown options
    dropdown_options = {
        "Kundendaten_Type": ["volatile Erzeugung 1", "volatile Erzeugung 2", "volatile Erzeugung 3", "Jvolatile Erzeugung 4", 
                               "steurbare Erzeugung 1", "steurbare Erzeugung 2", "steurbare Erzeugung 3", "steurbare Erzeugung 4", "Netzbezug"],
        "Kundendaten_Status": ["An", "Aus"]
    }

    return fields, predefined_fields, dropdown_options

def cal_jahresbenutzungsdauer(fields):
    """
    Calculate the annual usage duration based on the input fields.
    """
    try:
            # Get both values from the the fields
        energieverbrauch = float(fields["Energieverbrauch p.a. [kWh]"].get())
        maxJahresleistung = float(fields["Energieverbrauch p.a. [kWh]"].get())

        # Avoid division by zero
        if maxJahresleistung > 0:    
            return round(energieverbrauch / maxJahresleistung, 2)
        else:
            return "0.00"
    except ValueError:
        return "Fehler"