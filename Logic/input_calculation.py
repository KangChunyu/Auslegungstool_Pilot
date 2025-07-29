from Utils.dropdowns import *


def calculate_jahresbenutzungsdauer(energieverbrauch, max_leistung):
    if energieverbrauch > 0 and max_leistung > 0:
        return round(energieverbrauch / max_leistung, 2)
    return 0.00

def calculate_plausibilisierung_kaskade(herstellername, gesamt_kaskade):

    # Define maximum all kaskades for hersteller
    max_ecocoach = 6
    max_adstec = 5

    # Check the plausibility based on herstellername
    if herstellername == HERESTELLERNAME_OPTIONS[1]: # If the user pick "ecocoach" as herstellername
        return "Summe Kaskade korrekt" if gesamt_kaskade <= max_ecocoach else "Anzahl Kaskade zu hoch"
    elif herstellername == HERESTELLERNAME_OPTIONS[2]: # If the user pick "adstec" as herstellername
        return "Summe Kaskade korrekt" if gesamt_kaskade <= max_adstec else "Anzahl Kaskade zu hoch"
    else:
        return "Unbekannter Herstellername"    