#listarakenne
my_list = [4,13,9,0,33,7]
tyhja_lista = []

#monikkorakenne
my_tuple = ("kevät", "kesä", "syksy", "talvi")  #tuple, eli monikko

viikko = ("ma", "ti", "ke", "to", "pe", "la", "su")

paiva = int(input("Anna viikonpäivän järjestysnumero 1-7"))

vkpv = viikko[paiva -1]

print(f"{paiva}. paiva on {vkpv}")

hedelmat = ("banaani", "mango", "omeana")
(h1, h2, h3) = hedelmat   #stringi eli merkkijono

print("Hedelmä 1 on", h1)
print("Hedelmä 2 on", h2)
print("Hedelmä 3 on", h3)



import random

def heita():
    eka = random.randint(1,6)
    toka = random.randint(1,6)
    return(eka, toka)

noppa1, noppa2 = heita()
print(f"Nopista tuli {noppa1} ja {noppa2}. Liiku siis {noppa1+noppa2} askelta")




#koordinaatisto
def make_coordinates (x, y):
    return (x, y)

xcoordinate = int(input("Anna X koordinaatti"))
ycoordinate = int(input("Anna Y koordinaatti"))

point = make_coordinates(xcoordinate, ycoordinate)
print(point)


#joukko, eli SET
games = {"monopoly", "shakki", "cledos"}
games.add("WoW")
games.remove("WoW")
for p in games:
    print(p)

my_set = {"Mersu", "Mese", "A-ryhmä"}
tyhja_joukko = set()

#Sanakirja, eli DICTIONARY
my_dictionary = {
    "Matti" : [2, 1, 3, 5, 2],
    "Pekka" : [4, 5, 4, 4, 3],
    "Teppo" : [1, 2, 1, 0]
}

numerot = {"Viivi" : "050",
           "Ahmed" : "040",
           "Pekka" : "030"
           }
numerot["Olga"] = "060"

for nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}")