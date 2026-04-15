lentoasemat = {}
while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")

    valinta = input("Valintasi: ")
    if valinta == "1":
        icao = input("Anna lentoaseman ICAO").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Tiedot tallenettu")

    elif valinta == "2":
        icao = input("Anna lentoaseman ICAO").upper()
        if icao in lentoasemat:
            print(f"ICAO-koodia {icao} vastaa lentoaseman {lentoasemat[icao]}")
        else:
            print("Kyseistä lentoasemaa ei löydy rekisteristä")

    elif valinta == "0":
        print("Ohjelma päättyy")
        break
    else:
        print("Virheellinen valinta, yritä uudelleen")
        break