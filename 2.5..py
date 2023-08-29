Leiviskät = int(input("Anna leiviskät: "))
Naulat = int(input("Anna naulat: "))
Luodit = int(input("Anna luodit "))

Leiviskät = 20 * Naulat
Naulat = 32 * Luodit
Luodit = Luodit * 13.3
yhteensä = Leiviskät+Naulat+Luodit

kilogrammat = str(yhteensä // 1000)
grammat = str(yhteensä % 1000)


print("Massa nykymittojen mukaan:" +kilogrammat+ "kilogrammaa ja" +grammat+ "grammaa")
