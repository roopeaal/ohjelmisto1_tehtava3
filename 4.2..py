
#ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = int(input("Tuumat senttimetreiksi: "))

while tuuma >= 0:
    print(tuuma * 2.54)
    tuuma = int(input("Tuumat senttimetreiksi: "))
print("Ohjelma lopetettu")


