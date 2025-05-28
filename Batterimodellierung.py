
# Enteladeleistung ideal * Entladewirkungsgrad(Input_Maske)
def Entladeleistung_real():
    pass


# Spalte M: IF(SOC[%] > dynamisch SOC[%] AND 
#               Messwerte > 0 AND
#               Leistung über LSK-Grenze = 0), then get 
#           MIN(SOC[%] - dynamisch SOC[%]) * Kapazität nominal[kwh] * 4, Messwerte, Gesamte Entladeleistung(Input_Maske)) 
#           Else IF(Leistung über LSK-Grenze > Gesamte Entladeleistung(Input_Maske)) then use Gesamte Entladeleistung(Input_Maske)
#           Else IF(Leistung über LSK-Grenze * (1 / Wirkungsgrad) > Gesamte Entladeleistung(Input_Maske)) then use Gesamte Entladeleistung(Input_Maske)#
#           Else use Leistung über LSK-Grenze * (1 / Wirkungsgrad)
def Enladeleistung_ideal():
    
    pass

# Spalten U
def Ladeleistung_ideal():

    pass

# Spalten AM
def Netzbezug_neu():

    pass


# Spalten AL
def Einspeisung():

    pass

# Messwerte(Lastgang + DC Lader+ AC Lader - PV Erzeugung - BHKW)
def Messwerte():

    pass


# If (Messwerte > Grenzlast/LSK-Grenze, Messwerte - Grenzlast/LSK-Grenze, 0)
def Leistung_Über_LSK_Grenze():

    pass


# Nur für Aranea geplant ---------- 
def Grenzlast_LSK_Grenze():

    pass