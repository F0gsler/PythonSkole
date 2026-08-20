"""2.7 Operators."""

import sys


def afslut():
    print("Afslutter scriptet.")
    sys.exit()


def laes_tal(besked):
    while True:
        tekst = input(besked)
        try:
            return float(tekst)
        except ValueError:
            print("Fejl: Indtast venligst et gyldigt tal.")


def beregn(valg, a, b):
    if valg == "1":
        return "+", a + b
    if valg == "2":
        return "-", a - b
    if valg == "3":
        return "*", a * b
    return "/", a / b


def vis():
    while True:
        print("1: Addition")
        print("2: Subtraktion")
        print("3: Multiplikation")
        print("4: Division")
        print("5: Afslut")
        valg = input("Vælg en operation (1-5): ").strip()

        if valg == "5":
            afslut()

        if valg not in ["1", "2", "3", "4"]:
            print("Ugyldigt valg. Prøv igen.")
            continue

        a = laes_tal("Indtast første tal: ")
        b = laes_tal("Indtast andet tal: ")

        if valg == "4" and b == 0:
            print("Fejl: Der kan ikke divideres med 0.")
            continue

        operator, resultat = beregn(valg, a, b)
        print(f"Resultat: {a} {operator} {b} = {resultat}")


if __name__ == "__main__":
    vis()
