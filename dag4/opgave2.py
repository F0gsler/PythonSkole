"""2. Python matematisk og grafisk moduler (NumPy, Pandas, Matplotlib)."""

import numpy
import pandas

import sojle_diagram

elever = ["Marius", "Andreas", "Daniel", "Yosef", "Louie"]
fag = ["Python I", "Big Data I", "Serverside programmering"]
karakterer_7_trins_skala = [-3, 0, 2, 4, 7, 10, 12]


def main():
    tilfaeldige_karakterer = numpy.random.choice(
        karakterer_7_trins_skala,
        size=(len(elever), len(fag))
    )

    dataframe = pandas.DataFrame(tilfaeldige_karakterer, index=elever, columns=fag)

    for elev in elever:
        print(elev + " fik følgende karakterer:")
        for enkelt_fag in fag:
            karakter = dataframe.loc[elev, enkelt_fag]
            print("  " + enkelt_fag + ": " + str(karakter))
        print()

    gennemsnit = dataframe.mean()

    sojle_diagram.generer_soejle_diagram(
        fag,
        gennemsnit,
        "Gennemsnit pr. fag",
        "Fag",
        "Karaktergennemsnit"
    )


if __name__ == "__main__":
    main()