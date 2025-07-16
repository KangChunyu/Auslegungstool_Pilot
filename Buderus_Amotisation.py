import pandas as pd
from Input_Kundendaten import *

# Spalten F
def Laspitzkappung():
    """
    Calculate the Laspitzkappung based on the provided DataFrame.
    This function is the first table of the Buderus Amortisation tabs in tools
    """

    try:
        # Check if the DataFrame is loaded
        if 'kundendaten_df' not in globals():
            raise ValueError("kundendaten_df is not defined. Please load the DataFrame first.")

        # Netzbezug neu > 0 in Batteriemodellierung
        votaile_Erzeugung_Energie 
        # Max Leistung in Batteriemodellierung
        votaile_Erzeugung_Leistung  

        votaile_Erzeugung_Summe = votaile_Erzeugung_Energie / votaile_Erzeugung_Leistung 
        return votaile_Erzeugung_Summe

    except ValueError:
        print(f"Error")
