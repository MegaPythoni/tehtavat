hedelmat = {
    "mango" : 3.99,
    "banaani" : 1.20,
    "omena" : 0.5
              }

yhteishinta = 0

while True:
    hedelma = input("Anna hedelmä, jonka hinnan haluat tarkistaa (tyhjä lopettaa): ")

    if hedelma == "":
        print("Tilaus päättyy")
        break
    if hedelma in hedelmat:
        print(f"{hedelma}n kilohinta on {hedelmat[hedelma]}€")
        yhteishinta += hedelmat[hedelma]
    else:
        print("Tuotetta ei ole")
        lisataanko = input("Haluatko lisätä tuotteen ja hinnan (Y/N").upper()

        if lisataanko == "Y":
            hinta =float(input(f"Anna hinta {hedelma}lle:" ))
            hedelmat[hedelma] = hinta
            print (f"Hedelma on lisätty kilohinnalla {hinta}")

print ("Yhteishinta tilaukselle on", yhteishinta)

print("Päivitetty hinnasto: ")
for hedelma in hedelmat:
    print(f"{hedelma}, hinta: {hedelmat[hedelma]}")


