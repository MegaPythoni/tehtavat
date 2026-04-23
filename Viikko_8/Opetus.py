try:
    numero = int(input("Anna numero: "))
    jako = 10 / numero
    print(jako)
except ZeroDivisionError:
    print("Nollalla ei voi jakaa")
except ValueError:
    print("Kirjaimella ei voi jakaa")
finally:
    print("Tämä ajetaan aina")
    


