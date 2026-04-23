kirjasto = {
    "Sauluksen Matkat" : ["Sale", 26, "Elämänkerrat"],
    "Sorsan Seilaukset" : ["Terkkari", 26, "Utopiset Tarinat"],
}
print(f"Sauluksen Matkat on kirjoittanut {kirjasto["Sauluksen Matkat"][0]}")
print(f"Sorsan Seilaukset genre on{kirjasto["Sorsan Seilaukset"][2]}")
kirjasto["Joonas, tiskin ankkuri"] = ["Joonas", 26, "Rikollisuus"]
del kirjasto["Sauluksen Matkat"]
print("Kirjastossa on")
for nimi, tiedot in kirjasto.items():
    print(f"{nimi} : {tiedot}")