vuosiluku = int(input("Anna vuosiluku: "))
if vuosiluku % 4 == 0:
    if vuosiluku % 100 != 0 or vuosiluku % 400 == 0:
        print ("Tämä on karkausvuosi.")
    else:
        print("Tämä ei ole karkausvuosi.")

else:
    print("Tämä ei ole karkausvuosi.")