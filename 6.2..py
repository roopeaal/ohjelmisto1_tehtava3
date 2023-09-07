import random


def noppa(tahkot):
    luku = random.randint(1, tahkot)
    print(luku)

    while luku < tahkot:
        luku = random.randint(1, tahkot)
        print(luku)

    else:
        print("Sait maksimisilmäluvun, ohjelma päättyi")


tahkot = int(input("Anna nopan tahkojen yhteismäärä: "))
noppa(tahkot)
