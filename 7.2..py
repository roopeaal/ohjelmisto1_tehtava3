nimet = set()

while True:
    nimi = input("Syötä nimi: ")

    if not nimi:
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Syötit seuraavat nimet:")
for nimi in nimet:
    print(nimi)
