#Valintarakenne

#Tehtävä 1
print("Upea kuha! Olisi mahtavaa katsoa riittääkö sen pituus vai lasketko sen takaisin järveen!")
kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä:"))
if kuhan_pituus <=37:
    print(f"Kuhasi on:{37-kuhan_pituus} senttimetriä liian lyhyt, laske se takaisin")
else:
    print(f"Kuhasi on syötävä, ota se talteen")

#Tehtävä 2
print("Tervetuloa Silja Linelle, katsotaan missä on hyttisi")
hyttisi = input("Anna hyttisi(LUX,A,B vai C:")

if hyttisi == "LUX":
    print ("Parvekkeellinen hytti")
elif hyttisi == "A":
    print ("ikkunallinen hytti autokannen yläpuolella.")
elif hyttisi == "B":
    print ("ikkunaton hytti autokannen yläpuolella.")
elif hyttisi == "C":
    print("ikkunaton hytti autokannen alapuolella." )
else:
    print("Virheellinen hyttiluokka")

#Tehtävä 3
print("Katsotaan onko hemoglobiinisi kunnossa.")
sukupuoli = input("Anna sukupuolesi (nainen/mies:")
hemoglobiini = int(input("Anna hemoglobiinisi:"))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiinisi on alhainen")
    elif 117 <= hemoglobiini <=175:
        print("Hemoglobiinisi on normaali")
    else :
        print("Hemoglobiinisi on korkea")
if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiinisi on alhainen")
    elif 134 <= hemoglobiini <=195:
        print("Hemoglobiinisi on normaali")
    else :
        print("Hemoglobiinisi on korkea")

#Tehtävä 4
print("Anna minulle haluamasi vuosiluku, niin katsotaan onko se karkausvuosi")
vuosiluku = int(input("Anna vuosilukusi:"))

if (vuosiluku % 4 == 0 and vuosiluku % 100 !=0) or (vuosiluku % 400 ==0):
    print(f"Vuosi {vuosiluku} on karkausvuosi")
else:
    print(f"Vuosi {vuosiluku} ei ole karkausvuosi")