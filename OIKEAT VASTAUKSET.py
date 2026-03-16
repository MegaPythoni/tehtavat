tehtävä 4
import random

N = int(input("Anna arvottavien pisteiden määrä: "))
n = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1

pi_likiarvo = 4 * n / N
print("Piin likiarvo:", pi_likiarvo)

tehtävä 5 a)

import random

n = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for _ in range(n):
    summa += random.randint(1, 6)

print("Silmäluvut yhteensä:", summa)

b)
luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(float(syote))

luvut.sort(reverse=True)
print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)

c)
luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Ei ole alkuluku")
else:
    alkuluku = True
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("On alkuluku")
    else:
        print("Ei ole alkuluku")

d)
kaupungit = []

for _ in range(5):
    kaupungit.append(input("Anna kaupungin nimi: "))

print("Kaupungit:")
for k in kaupungit:
    print(k)


teht 6a)
import random

def heita_noppaa():
    return random.randint(1, 6)

while True:
    tulos = heita_noppaa()
    print(tulos)
    if tulos == 6:
        break

b)
import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

max_silma = int(input("Anna nopan maksimisilmä: "))

while True:
    tulos = heita_noppaa(max_silma)
    print(tulos)
    if tulos == max_silma:
        break

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    g = float(input("Anna gallonamäärä: "))
    if g < 0:
        break
    print("Litroina:", gallonat_litroiksi(g))

d)
def listan_summa(lista):
    return sum(lista)

luvut = [1, 2, 3, 4, 5]
print("Summa:", listan_summa(luvut))

e)
def parilliset(lista):
    return [x for x in lista if x % 2 == 0]

luvut = [1, 2, 3, 4, 5, 6]
print("Alkuperäinen:", luvut)
print("Parilliset:", parilliset(luvut))

f)
import math

def pizzan_hinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m**2
    return hinta / pinta_ala

p1_h = float(input("Pizza 1 halkaisija: "))
p1_e = float(input("Pizza 1 hinta: "))
p2_h = float(input("Pizza 2 halkaisija: "))
p2_e = float(input("Pizza 2 hinta: "))

h1 = pizzan_hinta(p1_h, p1_e)
h2 = pizzan_hinta(p2_h, p2_e)

if h1 < h2:
    print("Pizza 1 on edullisempi")
else:
    print("Pizza 2 on edullisempi")


7a)
vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kk = int(input("Anna kuukauden numero: "))

if kk in (12, 1, 2):
    print("talvi")
elif kk in (3, 4, 5):
    print("kevät")
elif kk in (6, 7, 8):
    print("kesä")
else:
    print("syksy")

7b)
nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Kaikki nimet:")
for n in nimet:
    print(n)

7c)
kentat = {}

while True:
    valinta = input("Lisää / Hae / Lopeta: ").lower()

    if valinta == "lisää":
        icao = input("ICAO-koodi: ")
        nimi = input("Kentän nimi: ")
        kentat[icao] = nimi

    elif valinta == "hae":
        icao = input("ICAO-koodi: ")
        print(kentat.get(icao, "Ei löytynyt"))

    elif valinta == "lopeta":
        break

9)
class Auto:
    def __init__(self, rek, huippu):
        self.rek = rek
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.huippu, self.nopeus + muutos))

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

13)
from flask import Flask, jsonify

app = Flask(__name__)

def on_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    return jsonify({"Number": luku, "isPrime": on_alkuluku(luku)})

app.run(port=3000)
