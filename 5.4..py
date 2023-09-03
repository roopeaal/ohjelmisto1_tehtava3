# Alustetaan tyhjä lista kaupungeille
kaupungit = []

# Kysytään käyttäjältä viisi kaupungin nimeä
for i in range(5):
    kaupunki = input("Syötä kaupungin nimi: ")
    kaupungit.append(kaupunki)

# Tulostetaan kaupunkien nimet yksi kerrallaan
print("Kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)
