#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa
# lukuaan arvauskertojen välissä.

import random
luku = int(random.randint(1, 10))

arvaus= int(input("Arvaa lukuni (1-10): "))
while arvaus < luku:
   print("Voi ei :( Liian pieni arvaus, yritä uudestaan")
   arvaus = int(input("Arvaa lukuni (1-10): "))
while arvaus > luku:
   print("Voi ei! :( Liian suuri arvaus, yritä uudestaan")
   arvaus = int(input("Arvaa lukuni (1-10): "))

else:
    print("Wau! Arvasit oikein! :)")