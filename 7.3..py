# Alustetaan tyhjä sanakirja lentoasemille
lentoasemat = {}

while True:
    print("Valitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valitse numero (1/2/3): ")

    if valinta == "1":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao_koodi] = nimi
        print("Lentoasema tallennettu!")

    elif valinta == "2":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi, jonka tiedot haluat hakea: ")
        nimi = lentoasemat.get(icao_koodi)
        if nimi:
            print(f"Lentoaseman nimi: {nimi}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        break

    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")

print("Ohjelma päätetty.")
