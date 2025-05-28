from Input_Kundendaten import kundendaten_df, bhkw_df

def Sorce_column():
    # Hier können Sie die Logik für die Quellspalte implementieren
    pass

def Sorce_unit():
    # Hier können Sie die Logik für die Quellspalte implementieren
    pass

def Sorce_row():
    # Hier können Sie die Logik für die Quellspalte implementieren
    pass


# (-1)*(Steuerbare_Erzeugung 1 bis 4) - BHKW[BHKW]
def Steurbare_Erzeugung():
    Ste_1 = 0
    Ste_2 = 0
    Ste_3 = 0
    Ste_4 = 0
    Total_BHKW = bhkw_df['BHKW'].sum()  # Sum of the 'BHKW' column

    Total_Result = (-1)*(Ste_1 + Ste_2 + Ste_3 + Ste_4) - Total_BHKW
    return Total_Result

# (-1)*(Volatile_Erzeugung 1 bis 4) - PV[PV2:Erzeuger]
def Summe_volatile_Erzeugung():
    Voe_1 = 0
    Voe_2 = 0
    Voe_3 = 0
    Voe_4 = 0
    Total_PV = PV_df['PV2:Erzeuger'].sum()  # Sum of the 'PV2:Erzeuger' column

    Total_Result = (-1)*(Voe_1 + Voe_2 + Voe_3 + Voe_4) - Total_PV
    return Total_Result

# 
def Einspeisung():
    # Hier können Sie die Berechnung für die Einspeisung implementieren
    pass

def PV1_Erzeuger():
    # (PV1:Hilfsspalte 2 interpoliert, normiert / 1000) * Input_Maske[Nennleistung [kWp]] * Input_Maske[Summer der Anteil PV-Fläche Ausrichtung(1&2)]
    PV1_df = PV_df['PV1:Hilfsspalte 2 interpoliert, normiert'] / 1000
    Total_PV1 = PV1_df.sum() 
    
    Total_Result = Total_PV1* Nennleistung * (Anteil_PV_Ausrichtung_1 + Anteil_PV_Ausrichtung_2)
    return Total_Result
    
def BHKW():
    Total_Result =bhkw_df['BHKW'].sum()
    return Total_Result

# =INDIRECT(ADDRESS($K6,AA$1,1,1,"Input Kundendaten"))*AA$2*AA$3+IFERROR('Input Kundendaten'!J10*4,0)
def Lastgang():
    return


#= AA6   + Q6   + V6   - AB6 + BA6 + $BC$2 +BD6+BE6
#  - IFERROR(Timeseries_49_225_9_137_SA_1kWp_crystSi_14_25deg_0deg_2015_20156[@[PV1: Erzeuger '[kW']]], 0)
#  - IFERROR(Tabelle6[@[PV2: Erzeuger '[kW']]], 0)
def Gesamtlast():
    # Hier können Sie die Berechnung für die Gesamtlast implementieren
    pass

# INDIRECT(ADDRESS($K6, Source column,1,1,"Input Kundendaten")) * Source Unit * Source Row + IFERROR('Input Kundendaten'!J10*4,0)
def Netzbezug():
    # Hier können Sie die Berechnung für den Netzbezug implementieren
    pass
