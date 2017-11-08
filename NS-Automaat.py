    #Kijkt naar het eerste station en gelij naar dat het laatste station niet als beginstation opgegeven word.
def inlezen_beginstation(stations):
    stationsNaam = input("Uw Beginstation: ")
    if stationsNaam in stations:
        if stationsNaam == "Maastricht":
            print("Dit is het eindstation, u kan hier niet beginnen.")
            stationsNaam = ''
    else:
        print("Dit station bestaat niet, Probeer het opnieuw")
        stationsNaam = ''
    return stationsNaam

    #Vraagt naar het laatste station, en kijk of de gebruiker geen station ingeeft dat voor het beginstation is.
def inlezen_eindstation(stations, beginstation):
    stationsNaam = input("Uw Eindstation: ")
    if stationsNaam not in stations or stations.index(beginstation) >= stations.index(stationsNaam):
        print("Probeer het opnieuw, dit station bestaat niet of is niet bereikbaar vanaf uw beginstation")
        stationsNaam = ''

    return stationsNaam

    #Print de tussenstations van de reis.
def omroepen_reis(stations, beginstation, eindstation):
    stationBeginNummer = stations.index(beginstation) + 1
    stationEindNummer = stations.index(eindstation) + 1
    afstandStations = stations.index(eindstation) - stations.index(beginstation)

    print("Het beginstation " + beginstation + " is het " + str(stationBeginNummer) + "e station in het traject.")
    print("Het eindstation " + eindstation + " is het " + str(stationEindNummer) + "e station in het traject.")
    if stationBeginNummer + 1 is not stationEindNummer:
        print("De afstand bedraagt " + str(afstandStations) + " station(s).")
    print("De prijs van het kaartje is " + str(afstandStations * 5) + " euro.")
    print("U stapt in de trein in: " + beginstation)
    for station in range(stationBeginNummer, stationEindNummer - 1):
        print('  -{}'.format(stations[station]))
    print("U stapt uit de trein in: " + eindstation)

stations = [
    "Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk",
    "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven",
    "Weert", "Roermond", "Sittard", "Maastricht"
]

while True:
    while True:
        beginStation = inlezen_beginstation(stations)
        if beginStation is not '':
            break

    while True:
        eindStation = inlezen_eindstation(stations, beginStation)
        if eindStation is not '':
            break

    omroepen_reis(stations, beginStation, eindStation)