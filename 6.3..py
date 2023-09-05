def yksi():
    gallona = int(input("Anna bensiinin määrän Yhdysvaltain nestegallonoina: "))
    while gallona >= 0:
        litra = gallona * 3.785
        print(f"{gallona} gallonaa on {litra} litraa.")
        gallona = int(input("Anna bensiinin määrän Yhdysvaltain nestegallonoina: "))
    else:
        print("Syötit negatiivisen gallonamäärän, ohjelma lopetettu.")

yksi()