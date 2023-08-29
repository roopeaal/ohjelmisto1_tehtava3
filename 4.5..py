oikea_kayttajatunnus = "python"
oikea_salasana = "rules"
yritykset = 5

while yritykset >0:
    käyttäjätunnus = input(("Käyttäjätunnus: "))
    salasana = input(("Salasana: "))

    if käyttäjätunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset -= 1
        if yritykset > 0:
            print("Väärä käyttäjätunnus tai salasana")
        else:
            print("Pääsy evätty")
