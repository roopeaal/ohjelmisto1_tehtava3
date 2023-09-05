import math

def laske_yksikkohinta(halkaisija, hinta):
    pizzan_pinta_ala = math.pi * ((halkaisija / 2) ** 2)
    yksikkohinta = hinta / pizzan_pinta_ala
    return yksikkohinta

def main():
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

    halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna toisen pizzan hinta (€): "))

    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
        print(f"Yksikköhinta: {yksikkohinta1:.2f} €/m²")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
        print(f"Yksikköhinta: {yksikkohinta2:.2f} €/m²")
    else:
        print("Molemmat pizzat ovat samanarvoisia yksikköhinnaltaan.")

if __name__ == "__main__":
    main()

def tervehdi():
    print("Moi!")
    tervehdi2()
    return

def tervehdi2 ():
    print("MOROO!")

print("Päivä alkaa tervehdyksellä.")
tervehdi()
print("Sitten siirrytään muihin asioihin.")
