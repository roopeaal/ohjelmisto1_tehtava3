luvut = []
luku = int(input("Anna luku: "))
while True:
    luvut.append(luku)
    luku = int(input("Anna seuraava luku tai lopeta painamalla Enter "))

    if luku == "":
        break
print(luvut)

