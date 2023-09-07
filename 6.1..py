import random
def noppa():
    luku = int(random.randint(1, 6))
    print(luku)

    while luku < 6:
        luku = int(random.randint(1, 6))

        print(luku)

    else:
        print("Sait luvun kuusi, ohjelma päättyi.")

noppa()