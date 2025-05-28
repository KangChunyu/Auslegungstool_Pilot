import pandas as pd
from Input_Kundendaten import *
from Kundendaten_verarbeitet import *
from Batterimodellierung import *
from Input_MaskeConfig import fields, predefined_fields


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
                       + PV1_Erzeuger() + PV2_Erzeuger() + BHKW())

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
        Jahresbenutzungsdauer
        Jahresbenutzungsdauer_ohne_Speicher
        Jahersbenutzungsdauer_mit_Speicher


