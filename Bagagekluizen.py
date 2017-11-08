kluizenBestand = open('Geregistreerde kluizen.txt', 'r')
bestand = kluizenBestand.read().splitlines()
kluizenBestand.close

#Menu
    #Optie 1
    #Geeft weer hoeveel kluizen er nog beschikbaar zijn
def aantalKluizenVrij():
    totaalAantalKluizen = 12
    res = totaalAantalKluizen - (len(bestand))
    return res

    #Optie 2
    #Kluis geristreren (let op er zijn maar 12 kluizen)
def nieuwe_kluis():
    maximaalKluizen = 12
    vrijeKluizenLijst = list(range(1, maximaalKluizen + 1))
    if aantalKluizenVrij() <= 0:
        print("Er zijn geen kluizen vrij.")

    if aantalKluizenVrij() > 0:
        for kluis in bestand:
            vrijeKluizenLijst.remove(int(kluis.split(';')[0]));
        nieuwe_kluis = vrijeKluizenLijst[0]
        print("Kluisnummer " + str(nieuwe_kluis) + " is voor u gekozen.")
        wachtwoord = input("Kies een wachtwoord: ")
        bestand.append(str(nieuwe_kluis) + ';' + str(wachtwoord))
        print('De kluis is geregistreerd!')
        save(bestand)

    #Optie 3
    #Haalt de kluis op
def magDeKluisOpen(kluisnummer, wachtwoord, kluis):
        return (str(kluisnummer) + ";" + str(wachtwoord) == kluis

def open_kluis():
    kluisnummer = input("Uw kluisnummer: ")
    wachtwoord = input("Wachtwoord: ")
    gevonden = false;
    for kluis in bestand:
        gevonden =  gevonden or magDeKluisOpen(kluisnummer, wachtwoord, kluis)

    if gevonnden:
        print("Uw kluis is nu open!")
    else:
        print("Uw wachtwoord/kluisnummer is niet juist.")


    #Optie 4
    #Levert de kluis in zodat iemand anders deze kan registreren
def kluis_teruggeven():
    kluisnummer = input("Uw kluisnummer: ")
    wachtwoord = input("Wachtwoord: ")
    for kluis in bestand:
        if magDeKluisOpen(kluisnummer, wachtwoord, kluis):
            bestand.remove(kluis)
            save(bestand)
            print('Uw kluis is open en wordt uit het systeem verwijderd')
            return

    print("Uw wachtwoord/kluisnummer is niet juist.")

#Bestand overschrijven
def save(bestand):
    kluizenBestand = open("Geregistreerde kluizen.txt","w")
    for line in bestand:
        kluizenBestand.write(line)
        kluizenBestand.write('\n')

    kluizenBestand.close()

def display_menu():
    while True:
        print('\n'
            'Kies een van de volgende opties:\n'
            '1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
            '2: Ik wil een nieuwe kluis\n'
            '3: Ik wil iets uit mijn kluis halen\n'
            '4: Ik geef mijn kluis terug\n'
            '\n')
        keuze = input('Geef uw optie:')

        if keuze == '1':
            print('Aantal kluizen vrij:' + ' ' + str(aantalKluizenVrij()))
        elif keuze == '2':
            nieuwe_kluis()
        elif keuze == '3':
            open_kluis()
        elif keuze == '4':
            kluis_teruggeven()
        else:
            print('Maak een geldige keuze.')

display_menu()