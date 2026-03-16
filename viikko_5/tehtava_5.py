#Tehtävä 1

import random

lukum = int(input("Anna arpakuutioiden lukumäärä"))
summa = 0

for _ in range(lukum):
    summa += random.randint(1,6)

print ("Silmäluvut yhteensä on",summa)

#Tehtävä 2
luvut = []

while True:
    syote = input("Anna lukuja, lopeta syöttämällä ###")
    if syote == "###":
        break
    luvut.append(float(syote))

luvut.sort(reverse=True)
print("Viisi suurinta lukua:")
for luku in luvut [:5]:
    print(luku)

#Tehtävä 3
anna = int(input("Anna luku niin kerron, onko se kokonaisluku"))
import math
if anna < 1:
    print ("Luku ei ole alkuluku")
else:
    alkuluku = True
    for i in range (1, int(anna**0.5) + 1):
        if alkuluku % i == 0:
            alkuluku = False
            break

if alkuluku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")

#Tehtävä 4

print ("Nyt tulostellaan kaupunkien nimiä")

kaupunki = []

for _ in range (5):
    kaupunki.append(input("Anna kaupungin nimi"))

print("Kaupungit järjestyksessä ovat:")
for k in kaupunki:
    print(k)
