import random

def laske_pi(n):
    neliön_sisällä = 0
    ympyrän_sisällä = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        neliön_sisällä += 1

        if x**2 + y**2 < 1:
            ympyrän_sisällä += 1

    arvioitu_pi = 4 * ympyrän_sisällä / neliön_sisällä
    return arvioitu_pi

try:
    arvottavien_pisteiden_maara = int(input("Syötä arvottavien pisteiden määrä: "))
    if arvottavien_pisteiden_maara <= 0:
        print("Pistelukumäärän tulee olla positiivinen.")
    else:
        arvioitu_pi = laske_pi(arvottavien_pisteiden_maara)
        print(f"Laskettu likiarvo pi:lle {arvioitu_pi}")
except ValueError:
    print("Virheellinen syöte. Syötä positiivinen kokonaisluku.")
