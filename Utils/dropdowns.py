'''
Dropdown options for various components in the application.
'''

# Kundendaten Types
KUNDENDATEN_OPTIONS = [
    "auswählen","volatile Erzeugung 1", "volatile Erzeugung 2", 
    "volatile Erzeugung 3", "volatile Erzeugung 4",
    "steuerbare Erzeugung 1", "steuerbare Erzeugung 2", 
    "steuerbare Erzeugung 3", "steuerbare Erzeugung 4", 
    "Netzbezug"
]

# Ertragsprofile for PV-Anlage
ERTRAGSPROFIL_OPTIONS = [
    "PVgis", "Standard", "Eigenprofil"
]

# Kundendaten Status
ANAUS_STATUS = ["An", "Aus"]

# Use Cases
USE_CASE_OPTIONS = ["Eigenverbrauch", "Netzstabilisierung", "Notstromversorgung"]

# Battery Use Cases
BATTERY_USE_CASE_OPTIONS = ["auswählen", "EVO", "LSK", "LSK & EVO"]

# Herstellername
HERESTELLERNAME_OPTIONS = ["Freitexteingabe", "Ecocoach", "Adc_tec Energy"]


# Ecocoach value mapping
ECOCOACH_VALUES = {
    "ecoBatteryHub 26kWh": {"kapazitaet_nominal": 26.0, "kapazitaet_nutzbar": 23.4, "ladeleistung": 16, "entladeleistung": 16, "wirkungsgrad": 0.93, "wartungskosten": 1.5},
    "ecoBatteryHub 32.5kWh": {"kapazitaet_nominal": 32.5, "kapazitaet_nutzbar": 29.3, "ladeleistung": 20, "entladeleistung": 20, "wirkungsgrad": 0.93, "wartungskosten": 1.5},
    "ecoBatteryHub 39kWh": {"kapazitaet_nominal": 39.0, "kapazitaet_nutzbar": 35.1, "ladeleistung": 25, "entladeleistung": 25, "wirkungsgrad": 0.93, "wartungskosten": 1.5},
    "ecoBatteryHub 45.5kWh": {"kapazitaet_nominal": 45.5, "kapazitaet_nutzbar": 41.0, "ladeleistung": 25, "entladeleistung": 25, "wirkungsgrad": 0.93, "wartungskosten": 1.5},
    "ecoBatteryHub 52kWh": {"kapazitaet_nominal": 52.0, "kapazitaet_nutzbar": 46.8, "ladeleistung": 25, "entladeleistung": 25, "wirkungsgrad": 0.93, "wartungskosten": 1.5},
    "ecoBatteryHub 58.5kWh": {"kapazitaet_nominal": 58.5, "kapazitaet_nutzbar": 52.7, "ladeleistung": 25, "entladeleistung": 25, "wirkungsgrad": 0.93, "wartungskosten": 1.5},
    "ecoBatteryHub 65kWh": {"kapazitaet_nominal": 65.0, "kapazitaet_nutzbar": 58.5, "ladeleistung": 25, "entladeleistung": 25, "wirkungsgrad": 0.93, "wartungskosten": 1.5},
}

# adc tec value mapping
ADC_VALUES = {
    "GSS0813": {"kapazitaet_nominal": 128.7, "kapazitaet_nutzbar": 111.6, "ladeleistung": 72, "entladeleistung": 16, "wirkungsgrad": 0.94, "wartungskosten": 0.0},
    "GSS0310": {"kapazitaet_nominal": 95.0, "kapazitaet_nutzbar": 86, "ladeleistung": 25, "entladeleistung": 20, "wirkungsgrad": 0.94, "wartungskosten": 0.0},
    "GSS0510": {"kapazitaet_nominal": 95.0, "kapazitaet_nutzbar": 86, "ladeleistung": 50, "entladeleistung": 25, "wirkungsgrad": 0.94, "wartungskosten": 0.0},
    "GSS0810": {"kapazitaet_nominal": 95.0, "kapazitaet_nutzbar": 86, "ladeleistung": 75, "entladeleistung": 25, "wirkungsgrad": 0.94, "wartungskosten": 0.0},
    "GSS0608": {"kapazitaet_nominal": 84.6, "kapazitaet_nutzbar": 74.7, "ladeleistung": 60, "entladeleistung": 25, "wirkungsgrad": 0.94, "wartungskosten": 0.0},
}

# Options for both Speicherbezeichnung (Ecocoach and ADC) (need to be after the value mappings)
SPEICHERBEZEICHNUNG_ECOCOACH_OPTIONS = list(ECOCOACH_VALUES.keys())
SPEICHERBEZEICHNUNG_ADC_OPTIONS = list(ADC_VALUES.keys())