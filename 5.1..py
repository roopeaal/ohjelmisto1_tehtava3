import random
lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0
for i in range(lukumaara):
    summa += random.randint(1,6)

print(summa)