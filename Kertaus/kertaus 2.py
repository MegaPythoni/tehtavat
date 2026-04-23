oppilaat = {
    "Matti" : ["Matti", 22, "Matikka"],
    "Teppo" : ["Teppo", 23, "Terveystieto"]
}
print(f"Matin vuosiluokka on: {oppilaat["Matti"][1]}")
print(f"Tepon lempiaine on: {oppilaat["Teppo"][2]}")

oppilaat["Matti"][2] = "Maantiede"
oppilaat["Matias"] = ["Matias", 20, "Musiikki"]
del oppilaat["Teppo"]

print("Päivitetty sanalista:")
for nimi, tiedot in oppilaat.items():
    print(f"{nimi}: {tiedot}")

