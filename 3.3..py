sukupuoli = input("Sukupuoli? (mies/nainen): ")
hemoglobiiniarvo = float(input("Hemoglobiiniarvo? (g/l): "))

if sukupuoli == "mies":
    alaraja = 134
    yläraja = 195
elif sukupuoli == "nainen":
    alaraja = 117
    yläraja = 175

if hemoglobiiniarvo < alaraja:
    print("Hemoglobiiniarvosi on alhainen")

elif hemoglobiiniarvo > yläraja:
    print("Hemoglobiiniarvosi on korkea")

else:
    print("Hemoglobiinirvosi on normaali")