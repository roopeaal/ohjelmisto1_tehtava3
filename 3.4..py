def on_karkausvuosi(vuosi):
    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        return True
    else:
        return False

vuosiluku = int(input("Syötä vuosiluku: "))

if on_karkausvuosi(vuosiluku):
    print(f"{vuosiluku} on karkausvuosi.")
else:
    print(f"{vuosiluku} ei ole karkausvuosi.")