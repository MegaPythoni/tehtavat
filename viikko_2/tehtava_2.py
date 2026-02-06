#Muuttujat ja vuorovaikutteiset ohjelma

#Tehtävä 1
print("Hei! Mukava nähdä sinua")
nimi = input("Mikä on nimesi?")
print("Hei", nimi)

#Tehtävä 2
import math
ympyra_sade = int(input("Mikä on ympyrän säde?"))
pi = math.pi
print("Hienoa, kiitos! Nyt lasken ympyrän pinta-alan.")
pinta_ala = (ympyra_sade*(pi**2))
print("Antamasi ympyrän pinta ala on:",pinta_ala)

#Tehtävä 3
print("Nyt ratkaistaan suorakulmion piiri ja pinta-ala")
kanta = int(input("Mikä on suorakulmion kanta?"))
korkeus = int(input("Mikä on suorakulmion korkeus?"))
print("Hienoa, kiitos! Nyt lasken suorakulmion pinta-alan ja piirin")
piiri = (kanta*2+korkeus*2)
ala = (kanta*korkeus)
print("Suorakulmion piri on:",piiri)
print("Suorakulmion kanta on:",ala)

#Tehtävä 4
kokonaisluku1 = int(input("Anna minulle kokonaisluku"))
kokonaisluku2 = int(input("Anna minulle toinen kokonaisluku"))
kokonaisluku3 = int(input("Anna minulle vielä kolmas kokonaisluku, sitten riittää"))
print("kokonaislukujen summa on",kokonaisluku1+kokonaisluku2+kokonaisluku3)
print("kokonaislukujen tulo on",kokonaisluku1*kokonaisluku2*kokonaisluku3)
print("kokonaislukujen keskiarvo on",(kokonaisluku1+kokonaisluku2+kokonaisluku3)/3)


#Tehtävä 5
print("Nyt ratkotaan muinainen mysteeri, eli painosi leivisköinä")
leiviskat = float(input("Anna minulle leiviskat?"))
naulat = float(input("Anna minulle naulat?"))
luodit = float(input("Anna minulle luodi?"))

yhteensa_grammat = (leiviskat*20*32*13.3)+(naulat*32*13.3)+(luodit*13.3)
kilot = int(yhteensa_grammat//1000)
grammat = (yhteensa_grammat%1000)

print(f"Painosi nykymittojen mukaan: {kilot} kilogrammaa ja {grammat:.2f} grammaa.")


#6 Tehtävä
print("Hienoa, nyt keksitään sinulle kaksi erilaista numerolukon koodia!")
print("Arvotaan...")
import random
luku1 = random.randint(0,9)
luku2 = random.randint(0,9)
luku3 = random.randint(0,9)
print(luku1, luku2, luku3)

print("Arvotaan toinen koodi...")
luku1_1 = random.randint(1,6)
luku2_1 = random.randint(1,6)
luku3_1 = random.randint(1,6)
luku4_1 = random.randint(1,6)
print(luku1_1, luku2_1, luku3_1, luku4_1)
