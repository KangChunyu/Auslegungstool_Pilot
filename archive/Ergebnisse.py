import pandas as pd
import tkinter as tk

from Input_Kundendaten import *
from archive.Kundendaten_verarbeitet import *
from Batterimodellierung import *
from archive.Input_MaskeConfig import *


def Check_value(value):
    """
    Check if the value is a number and return it as a float.
    If not, return 'Keine Angaben'.
    """
    return value if value is not None else "Keine Angaben"


# Calculate all columns in Ennergiefluesse Table 
def Energiefluesse():
    try:
        # Calculate Stromertrag
        Stromertrag = (-Steurbare_Erzeugung() - Summe_volatile_Erzeugung() + Einspeisung()
                       + PV1_Erzeuger() + BHKW())

        # Calculate Stromverbrauch
        Stromverbrauch = Lastgang()

        # Calculate Direkter Eigenverbrauch
        Direkter_Eigenverbrauch = Stromverbrauch - Gesamtlast()

        # =IFERROR(Batteriemodellierung!O35045,"keine Angaben")
        Eigenverbrauch_aus_Batterie = Check_value(Entladeleistung_real())
        # =IFERROR(Batteriemodellierung!AM35045,"keine Angaben")
        Netzbezug_mit_Speicher = Check_value(Netzbezug_neu())
        # =IFERROR(-Batteriemodellierung!AL35045,"keine Angaben")
        Neteinspeisung_nach_Speicher = - Check_value(Einspeisung())
        # =IFERROR(Batteriemodellierung!U35045-Batteriemodellierung!O35045,"keine Angaben")
        Wechselrichterverluste = Check_value(Ladeleistung_ideal() - Entladeleistung_real())

        # Return all values as a dictionary
        return {
            "Stromertrag": Stromertrag,
            "Stromverbrauch": Stromverbrauch,
            "Direkter Eigenverbrauch": Direkter_Eigenverbrauch,
            "Eigenverbrauch aus Batterie": Eigenverbrauch_aus_Batterie,
            "Netzbezug mit Speicher": Netzbezug_mit_Speicher,
            "Netzeinspeisung nach Speicher": Neteinspeisung_nach_Speicher,
            "Wechselrichterverluste": Wechselrichterverluste,
        }

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {
            "Stromertrag": "Keine Angaben",
            "Stromverbrauch": "Keine Angaben",
            "Direkter Eigenverbrauch": "Keine Angaben",
            "Eigenverbrauch aus Batterie": "Keine Angaben",
            "Netzbezug mit Speicher": "Keine Angaben",
            "Netzeinspeisung nach Speicher": "Keine Angaben",
            "Wechselrichterverluste": "Keine Angaben",
        }


# Calculate all values in Energiebezugsdaten Table
def Engergiebezugsdaten(fields):
    try:
        # Show the selection of Lastprofile from the user
        gewähltes_Lastprofil = "place for showing the result of the selection"
        # Retrives values from the fields dictionary
        Brutto_Stromkosten = Check_value(fields["Brutto_Sromkosten"].get())
        
        MaxJahrleistung_Lastprofil = Check_value(fields["max. Jahresleistung, Lastprofil [kW]"].get())
        # Get Value from Input_Maske
        Jahresbenutzungsdauer = Check_value(fields["Jahresbenutzungsdauer [h]"].get())
        # Get Value from function in Buderus_Amotisation
        Jahresbenutzungsdauer_ohne_Speicher = Check_value(Summe_volatile_Erzeugung())
        
        Jahersbenutzungsdauer_mit_Speicher_PV = Check_value(fields["Jahresbenutzungsdauer mit Speicher PV [h]"].get())

        return {
            "Gewähltes Lastprofil": gewähltes_Lastprofil,
            "Brutto Stromkosten": Brutto_Stromkosten,
            "Maximale Jahresleistung, Lastprofil [kW]": MaxJahrleistung_Lastprofil,
            "Jahresbenutzungsdauer [h]": Jahresbenutzungsdauer,
            "Jahresbenutzungsdauer ohne Speicher [h]": Jahresbenutzungsdauer_ohne_Speicher,
            "Jahresbenutzungsdauer mit Speicher PV [h]": Jahersbenutzungsdauer_mit_Speicher_PV,
        }
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {
            "Gewähltes Lastprofil": "Keine Angaben",
            "Brutto Stromkosten": "Keine Angaben",
            "Maximale Jahresleistung, Lastprofil [kW]": "Keine Angaben",
            "Jahresbenutzungsdauer [h]": "Keine Angaben",
        }


# Show all results 
if __name__ == "__main__":

    # Create a tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window since we are not using it for GUI


    # Retrieve the fields from Input_MaskeConfig
    fields, predefined_fields, dropdown_options = initialize_fields()

    # Calculate Energiefluesse
    print("Calculating Energiefluesse...")
    energie_fluesse = Energiefluesse()
    
    
    # Calculate Engergiebezugsdaten
    energie_bezugsdaten = Engergiebezugsdaten(fields)

    # Display results
    print("Energiefluesse:")
    for key, value in energie_fluesse.items():
        print(f"{key}: {value}")

    print("\nEnergiebezugsdaten:")
    for key, value in energie_bezugsdaten.items():
        print(f"{key}: {value}")


