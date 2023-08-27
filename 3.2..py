hyttiluokka = (input("Mikä hyttiluokka sinulla on? (LUX/A/B/C): "))
if hyttiluokka == "LUX":
    print("Sinulla on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("Sinulla on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("Sinulla on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("Sinulla on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")