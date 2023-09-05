def karsi_parittomat(lista):
    karsittu_lista = [luku for luku in lista if luku % 2 == 0]
    return karsittu_lista


def main():
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    alkuperainen_lista = luvut
    karsittu_lista = karsi_parittomat(luvut)

    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Karsittu lista (parilliset luvut):", karsittu_lista)


if __name__ == "__main__":
    main()
