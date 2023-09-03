# Alustetaan tyhjä lista lukuja varten
luvut = []

# Kysytään käyttäjältä lukuja
while True:
    syote = input("Syötä luku (tyhjä rivi lopettaa): ")

    # Tarkistetaan, onko syöte tyhjä
    if syote == "":
        break

    # Yritetään muuttaa syöte kokonaisluvuksi, ja lisätään se listaan
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte. Syötä kokonaisluku.")

# Tarkistetaan, onko lukuja annettu tarpeeksi
if len(luvut) < 5:
    print("Syötä vähintään viisi lukua.")
else:
    # Lajitellaan luvut suurimmasta pienimpään ja tulostetaan viisi suurinta
    luvut.sort(reverse=True)
    viisi_suurinta = luvut[:5]
    print("Viisi suurinta lukua suurimmasta alkaen:", viisi_suurinta)
