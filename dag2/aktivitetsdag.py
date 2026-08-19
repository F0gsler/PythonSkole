kapacitet = {"Gaming": 20, "3D-print": 15, "Robotbygning": 20, "Programmering": 25, "Sport": 30}

lokaler = {"Gaming": "Gaming-lab", "3D-print": "Lærere lounge", "Robotbygning": "Elektronikværksted", "Programmering": "Lokale 2.08", "Sport": "Parkeringsplads"}

laerere = {"Gaming": "Palle", "3D-print": "Henrik", "Robotbygning": "Søren", "Programmering": "Niels", "Sport": "Flemming"}


def mergeAktiviteter(kapacitet, lokaler, laerere):
    ny_dict = {key: {"max": value, "lokale": lokaler[key], "laerer": laerere[key]} for key, value in kapacitet.items()}
    return ny_dict

def læsTal(besked):
    tal = input(besked)
    while not tal.isdigit():
        print("Indtast et tal.")
        tal = input(besked)
    return int(tal)

def indlæsKlasser(antalKlasser):
    ny_dict = {}
    for nr in range(1, antalKlasser + 1):
        key = input(f"Navn på klasse {nr}: ")
        value = laesTal(f"Antal elever i {key}: ")
        ny_dict[key] = value
    return ny_dict

def antalElever(klasser):
    return sum(klasser.values())

def antalPladser(aktiviteter):
    ny_dict = {key: value["max"] for key, value in aktiviteter.items()}
    return sum(ny_dict.values())

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