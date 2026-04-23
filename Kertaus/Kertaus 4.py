import math


def create_point(x,y):
    return(x,y)
def distance(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    return d

print("Syötä pisteen 1 koordinaatit:")
p1 = create_point(float(input("x1: ")), float(input("y1: " )))
p2 = create_point(float(input("x2: ")), float(input("y2: ")))
tulos = distance(p1, p2)
print(f"\nEtäisyys pisteiden {p1} ja {p2} välillä on noin {tulos:.2f}")

