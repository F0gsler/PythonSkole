kapacitet = {"Gaming": 20, "3D-print": 15, "Robotbygning": 20, "Programmering": 25, "Sport": 30}

lokaler = {"Gaming": "Gaming-lab", "3D-print": "Lærere lounge", "Robotbygning": "Elektronikværksted", "Programmering": "Lokale 2.08", "Sport": "Parkeringsplads"}

laerere = {"Gaming": "Palle", "3D-print": "Henrik", "Robotbygning": "Søren", "Programmering": "Niels", "Sport": "Flemming"}


def mergeAktiviteter(kapacitet, lokaler, laerere):
    ny_dict = {navn: {"max": kapacitet[navn], "lokale": lokaler[navn], "laerer": laerere[navn]} for navn in kapacitet}
    return ny_dict

def laesTal(besked):
    tal = input(besked)
    while not tal.isdigit():
        print("Indtast et tal.")
        tal = input(besked)
    return int(tal)

def indlaesKlasser(antalKlasser):
    klasser = {}
    for nr in range(1, antalKlasser + 1):
        navn = input(f"Navn på klasse {nr}: ")
        elever = laesTal(f"Antal elever i {navn}: ")
        klasser[navn] = elever
    return klasser

def antalElever(klasser):
    ny_list = [elever for elever in klasser.values()]
    return sum(ny_list)

def antalPladser(aktiviteter):
    ny_list = [info["max"] for info in aktiviteter.values()]
    return sum(ny_list)

def helKlasse(aktiviteter, elever):
    ny_list = [navn for navn, info in aktiviteter.items() if info["max"] >= elever]
    return ny_list

def fordelKlasser(klasser, aktiviteter):
    ledig = {navn: info["max"] for navn, info in aktiviteter.items()}
    plan = {navn: [] for navn in aktiviteter}

    for klasse in klasser:
        for aktivitet in plan:
            if ledig[aktivitet] >= klasser[klasse]:
                plan[aktivitet].append(klasse)
                ledig[aktivitet] -= klasser[klasse]
                break
    return plan, ledig