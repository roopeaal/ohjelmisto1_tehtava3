def laske_summa(lista):
    summa = sum(lista)
    return summa


def main():
    luvut = [1, 2, 3, 4, 5]

    summa = laske_summa(luvut)
    print(f"Listan summa: {summa}")


if __name__ == "__main__":
    main()
