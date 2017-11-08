import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationsdict = processXML('stations.xml')
stations = stationsdict['Stations']['Station']

print('Dit zijn de codes en types van de 4 stations:')
for station in stations:
    code = str(station['Code'])
    type = str(station['Type'])
    print(code + ' - ' + type)

print('\nDit zijn alle stations met één of meer synoniemen:')
for station in stations:
    code = str(station['Code'])
    if station['Synoniemen'] is not None:
        synoniem = str(station['Synoniemen']['Synoniem'])
        print(code + ' - ' + synoniem)

print('\nDit is de lange naam van elk station:')
for station in stations:
    code = str(station['Code'])
    langeNaam = str(station['Namen']['Lang'])
    print(code + ' - ' + langeNaam)