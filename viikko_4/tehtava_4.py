#Alkuehdollinen toistorakenne

#Tehtävä 1
luku = 1
while luku <= 1000:
  if luku % 3 == 0:
      print(luku)
  luku += 1

#Tehtävä 2

while True:
  tuuma_sentiksi = int(input("Anna random tuuma:"))
  print(f"Antamasi tuuma {tuuma_sentiksi} on {tuuma_sentiksi * 2.54}cm, yritä uudelleen")
  if tuuma_sentiksi <0:
    print("Ohjelma loppui")
  break

#Tehtävä 3

pienin = None
suurin = None

while True:
  random_luku = (input("Anna random lukuja, tyhjä merkkijono (###) lopettaa pelin"))
  if random_luku == "###":
      break
  luku = int(random_luku)

  if pienin is None or luku < pienin:
      pienin = luku
  if suurin is None or luku > suurin:
      suurin = luku
if pienin is not None:
    print(f"Pienin luku on{pienin}")
    print(f"Suurin luku on{suurin}")
else:
    print("Et antannut lukuja")

#Tehtävä 4
print("Nyt arvotaan numeroita, ja katsotaan arvaatko numeroni")
import random
luku1 = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa numero 1-10 välillä:"))
    if arvaus < luku1:
        print ("Liian pieni")
    elif arvaus > luku1:
        print ("Liian suuri")
    else:
        print ("Oikein.")
        break

#Tehtävä 5
print("Tervetuloa, päästäksesi sisään syötä käyttäjätunnus ja pääsykoodi")
tunnus_oikein = "python"
salis_oikein = "rules"
yritykset = 0

while yritykset<5:
    kayttajatunnus = input("Anna käyttäjätunnus:")
    salasana = input("Anna salasana:")
    if kayttajatunnus == tunnus_oikein and salasana == salis_oikein:
        print("Tervetuloa")
        break
    else:
        yritykset +=1
        if yritykset <5:
            print(f"Väärin, sinulla on {5-yritykset} kertaa jäljellä")
else:
    print("Pääsy evätty")

#Tehtävä 6
print("Nyt luodaan algoritmi josta en tajunnut itsekään mitään, mutta sillä pitäisi selvitä pi:n likiarvo")

import math
import random
pi = math.pi

pisteet = int(input("Anna pisteiden määrä, jolla selvitän likiarvon"))
ympyralaA = float((pi*1)**2)
nelio_B_ala = (2*2)
suhde = ympyralaA / nelio_B_ala

while pisteet:
    random.randint ((0, ympyralaA)*1000)


