# Funktio, joka tarkistaa onko luku alkuluku
def onko_alkuluku(luku):
    if luku <= 1:
        return False  # 0 ja 1 eivät ole alkulukuja
    elif luku == 2:
        return True   # 2 on alkuluku
    else:
        # Tarkistetaan, onko luku jaollinen millään luvulla 2:n ja luvun itsensä välillä
        for i in range(2, luku):
            if (luku % i) == 0:
                return False
        return True

# Kysytään käyttäjältä luku
syote = input("Syötä kokonaisluku: ")

# Yritetään muuttaa käyttäjän syöte kokonaisluvuksi
try:
    luku = int(syote)
    if onko_alkuluku(luku):
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")
except ValueError:
    print("Virheellinen syöte. Syötä kokonaisluku.")
