#tehtava 1

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuu_numero = int(input("Anna haluamasi kuukausi numerona (1-12) "))

vastaus = vuodenajat[kuu_numero-1]

print(f"{kuu_numero}. kuukauden vuodenaika on {vastaus}")


#tehtava 2
nimet = set()
while True:
    nimi = input("Syötä nimi, tyhjä lopettaa: ")
    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)


#tehtävä 3
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




