"""2.8 Closures."""


def opret_rabatberegner(rabat_procent):
    def beregn_pris(pris):
        return pris - (pris * rabat_procent / 100)
    return beregn_pris


def opret_valutaomregner(kurs):
    def omregn(beloeb):
        return beloeb * kurs
    return omregn


def vis():
    rabat10 = opret_rabatberegner(10)
    rabat25 = opret_rabatberegner(25)
    print("500 kr. med 10% rabat:", rabat10(500))
    print("500 kr. med 25% rabat:", rabat25(500))

    euro_til_kroner = opret_valutaomregner(7.46)
    dollar_til_kroner = opret_valutaomregner(6.92)
    print("100 euro i kroner:", round(euro_til_kroner(100), 2))
    print("100 dollar i kroner:", round(dollar_til_kroner(100), 2))


if __name__ == "__main__":
    vis()
