
kuukaudet = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
kuukausi = kuukaudet[järjestysnumero-1]
print (f"{järjestysnumero}. kuukausi on {kuukausi}.")