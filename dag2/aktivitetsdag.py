"""1.5 Problemorienteret case: planlæg aktivitetsdagen på TEC."""

kapacitet = {"Gaming": 20, "3D-print": 15, "Robotbygning": 20, "Programmering": 25, "Sport": 30}

lokaler = {"Gaming": "Gaming-lab", "3D-print": "Lærere lounge", "Robotbygning": "Elektronikværksted",
           "Programmering": "Lokale 2.08", "Sport": "Parkeringsplads"}

laerere = {"Gaming": "Palle", "3D-print": "Henrik", "Robotbygning": "Søren",
           "Programmering": "Niels", "Sport": "Flemming"}


def mergeAktiviteter(kapacitet, lokaler, laerere):
    ny_dict = {key: {"max": value, "lokale": lokaler[key], "laerer": laerere[key]}
               for key, value in kapacitet.items()}
    return ny_dict


def laesTal(besked):
    tal = input(besked).strip()
    while not tal.isdigit():
        print("Indtast et tal.")
        tal = input(besked).strip()
    return int(tal)


def indlaesKlasser(antalKlasser):
    ny_dict = {}
    for nr in range(1, antalKlasser + 1):
        key = input(f"Navn på klasse {nr}: ").strip()
        value = laesTal(f"Antal elever i {key}: ")
        ny_dict[key] = value
    return ny_dict


def antalElever(klasser):
    return sum(klasser.values())


def antalPladser(aktiviteter):
    pladser = {key: value["max"] for key, value in aktiviteter.items()}
    return sum(pladser.values())


def helKlasse(aktiviteter, elever):
    ny_dict = {key: value["max"] for key, value in aktiviteter.items() if value["max"] >= elever}
    return ny_dict


def mulighederPrKlasse(aktiviteter, klasser):
    ny_dict = {key: helKlasse(aktiviteter, value) for key, value in klasser.items()}
    return ny_dict


def fordelKlasser(klasser, aktiviteter):
    ledig = {key: value["max"] for key, value in aktiviteter.items()}
    plan = {key: {} for key in aktiviteter.keys()}

    for klasse, elever in klasser.items():
        for aktivitet in plan.keys():
            if ledig[aktivitet] >= elever:
                plan[aktivitet][klasse] = elever
                ledig[aktivitet] -= elever
                break
    return plan, ledig


def vis():
    aktiviteter = mergeAktiviteter(kapacitet, lokaler, laerere)

    antalKlasser = laesTal("Hvor mange klasser deltager: ")
    klasser = indlaesKlasser(antalKlasser)

    elever = antalElever(klasser)
    pladser = antalPladser(aktiviteter)

    print()
    print("Deltagende klasser:")
    for nr, klasse in enumerate(klasser, start=1):
        print(f"[{nr}] {klasse} med {klasser[klasse]} elever")
    print("Elever i alt:", elever)

    print()
    print("Aktiviteter:")
    for navn, info in aktiviteter.items():
        print(f"{navn}, max {info['max']} deltager, {info['lokale']}, {info['laerer']}")
    print("Pladser i alt:", pladser)

    if pladser >= elever:
        print("Der er plads nok til alle elever.")
    else:
        print("Der er ikke plads nok til alle elever.")

    print()
    print("Aktiviteter der kan rumme en hel klasse:")
    muligheder = mulighederPrKlasse(aktiviteter, klasser)
    for klasse, aktivitet in muligheder.items():
        print(f"{klasse}:", list(aktivitet.keys()))

    print()
    print("Forslag til fordeling:")
    plan, ledig = fordelKlasser(klasser, aktiviteter)
    for aktivitet in plan:
        print(f"{aktivitet}:", plan[aktivitet], f"({ledig[aktivitet]} pladser tilbage)")


if __name__ == "__main__":
    vis()
