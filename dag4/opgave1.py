import csv
import html
import os
import re

import requests

API_URL = "https://api.fbi.gov/wanted/v1/list"
PAGE_SIZE = 50

# FBI's api afviser kald uden en almindelig User-Agent header.
HEADERS = {"User-Agent": "Mozilla/5.0 (PythonSkole opgave)"}

# Opgaveteksten naevner "Most Wanted Fraudster" og "ViCAP Missing Persons",
# mens skaermbillederne viser "Criminal Enterprise Investigations".
# Derfor hentes og vises alle tre subjects.
SUBJECTS = [
    ("Most Wanted Fraudster", "last seen", "Enter last seen location: "),
    ("Criminal Enterprise Investigations", "Gang name", "Enter gang name: "),
    ("ViCAP Missing Persons", "last seen", "Enter last seen location: "),
]

SUBJECT_NAVNE = [navn for navn, felt, spoerg in SUBJECTS]

MAPPE = os.path.dirname(os.path.abspath(__file__))
CSV_FIL = os.path.join(MAPPE, "fbi_data.csv")
OPDATERING_FIL = os.path.join(MAPPE, "opdateringer.csv")


def rens_tekst(tekst):
    if tekst is None:
        return ""
    tekst = re.sub("<[^>]*>", " ", str(tekst))
    tekst = html.unescape(tekst)
    tekst = tekst.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    tekst = re.sub(" +", " ", tekst)
    return tekst.strip()


def lav_tekst_af_liste(liste):
    if liste is None:
        return ""
    tekster = []
    for element in liste:
        tekster.append(rens_tekst(element))
    return "; ".join(tekster)


def hent_data_fra_api():
    personer = []
    side = 1

    while True:
        svar = requests.get(
            API_URL,
            params={"page": side, "pageSize": PAGE_SIZE},
            headers=HEADERS,
            timeout=30,
        )
        svar.raise_for_status()
        data = svar.json()

        items = data.get("items", [])
        if len(items) == 0:
            break

        for item in items:
            subjects = item.get("subjects")
            if subjects is None:
                continue
            if not any(navn in subjects for navn in SUBJECT_NAVNE):
                continue

            person = {
                "subjects": lav_tekst_af_liste(subjects),
                "title": rens_tekst(item.get("title")),
                "aliases": lav_tekst_af_liste(item.get("aliases")),
                "details": rens_tekst(item.get("details")),
            }
            personer.append(person)

        total = data.get("total", 0)
        if side * PAGE_SIZE >= total:
            break
        side = side + 1

    return personer


def gem_csv(personer):
    with open(CSV_FIL, "w", newline="", encoding="utf-8") as fil:
        writer = csv.writer(fil)
        writer.writerow(["subjects", "title", "aliases", "details"])
        for person in personer:
            writer.writerow([
                person["subjects"],
                person["title"],
                person["aliases"],
                person["details"],
            ])


def laes_csv():
    """Fallback: laes den tidligere gemte csv, hvis API'et ikke kan naas."""
    personer = []
    if not os.path.exists(CSV_FIL):
        return personer

    with open(CSV_FIL, encoding="utf-8") as fil:
        for raekke in csv.DictReader(fil):
            personer.append(raekke)
    return personer


def hent_opdateringer():
    opdateringer = {}
    if not os.path.exists(OPDATERING_FIL):
        return opdateringer

    with open(OPDATERING_FIL, encoding="utf-8") as fil:
        for raekke in csv.reader(fil):
            if len(raekke) == 2:
                opdateringer[raekke[0]] = raekke[1]
    return opdateringer


def gem_opdateringer(opdateringer):
    with open(OPDATERING_FIL, "w", newline="", encoding="utf-8") as fil:
        writer = csv.writer(fil)
        for navn in opdateringer:
            writer.writerow([navn, opdateringer[navn]])


def find_personer(personer, subject):
    fundne = []
    for person in personer:
        if subject in person["subjects"]:
            fundne.append(person)
    return fundne


def vis_og_opdater(personer, subject, felt_tekst, spoerg_tekst, opdateringer):
    fundne = find_personer(personer, subject)

    print()
    print(subject + ":")
    if len(fundne) == 0:
        print("(ingen personer fundet)")
        return

    for i in range(len(fundne)):
        navn = fundne[i]["title"]
        vaerdi = opdateringer.get(navn, "Unknown")
        print("[" + str(i + 1) + "] " + navn + ", " + felt_tekst + ": " + vaerdi)

    while True:
        valg = input("Select person to update (enter q to exit): ").strip()
        if valg.lower() == "q":
            return
        if valg.isdigit() and 1 <= int(valg) <= len(fundne):
            navn = fundne[int(valg) - 1]["title"]
            ny_vaerdi = input(spoerg_tekst).strip()
            if ny_vaerdi != "":
                opdateringer[navn] = ny_vaerdi
                gem_opdateringer(opdateringer)
            return
        print("Ugyldigt valg.")


def main():
    print("Henter data fra FBI API ...")
    try:
        personer = hent_data_fra_api()
        gem_csv(personer)
        print("Gemte " + str(len(personer)) + " personer i " + CSV_FIL)
    except requests.RequestException as fejl:
        print("Kunne ikke hente data fra API'et:", fejl)
        personer = laes_csv()
        if len(personer) == 0:
            print("Der er heller ingen gemt csv-fil at laese fra. Afslutter.")
            return
        print("Bruger i stedet de " + str(len(personer)) + " personer fra " + CSV_FIL)

    opdateringer = hent_opdateringer()

    while True:
        print()
        print("--------------------------------")
        for i in range(len(SUBJECTS)):
            print("[" + str(i + 1) + "] Show " + SUBJECTS[i][0])
        print("[q] Afslut")
        valg = input("Vælg 1, 2 eller 3: ").strip()

        if valg.lower() == "q":
            break

        if valg.isdigit() and 1 <= int(valg) <= len(SUBJECTS):
            navn, felt_tekst, spoerg_tekst = SUBJECTS[int(valg) - 1]
            vis_og_opdater(personer, navn, felt_tekst, spoerg_tekst, opdateringer)
        else:
            print("Ugyldigt valg.")


if __name__ == "__main__":
    main()