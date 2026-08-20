"""Grundlæggende Python programmering."""

import aktivitetsdag
import functions
import ovelse2_1
import ovelse2_2
import ovelse2_3
import ovelse2_4
import ovelse2_5
import ovelse2_6
import ovelse2_7
import ovelse2_8


def vis_comprehension():
    numbersList = [1, 2, 3, 4, 5]
    stringsList = ["apple", "an", "banana", "cat", "dog", "elephant"]
    numbersSets = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    wordsSets = {"apple", "banana", "cherry", "date", "grapefruit", "fig", "grape"}
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    students_scores = {"Thomas": 2, "Alex": 12, "Charlie": 10, "David": 4}

    print("# Comprehension: list af tal:")
    print("Original list:", numbersList)
    print("Comprehension kode brugt:", "[i ** 2 for i in numbersList]")
    print("Ny list:", functions.ComprehensionListNum(numbersList))

    print()
    print("# Comprehension: list af strings:")
    print("Original list:", stringsList)
    print("Comprehension kode brugt:", "[s for s in stringsList if len(s) > 3]")
    print("Ny list:", functions.ComprehensionListStr(stringsList))

    print()
    print("# Comprehension: sets af tal:")
    print("Original set:", numbersSets)
    print("Comprehension kode brugt:", "{i for i in numbersSets if i % 2 == 0}")
    print("Ny set:", functions.ComprehensionSetsNum(numbersSets))

    print()
    print("# Comprehension: set af strings:")
    print("Original set:", wordsSets)
    print("Comprehension kode brugt:", "{word[0] for word in wordsSets}")
    print("Ny set:", functions.ComprehensionSetsStr(wordsSets))

    print()
    print("# Comprehension: dictionary af 2 lister:")
    print("Original lister:", keys, values)
    print("Comprehension kode brugt:", "{k: v for k, v in zip(keys, values)}")
    print("Ny dictionary:", functions.ComprehensionDictKeysValues(keys, values))

    print()
    print("# Comprehension: dictionary af key value pair:")
    print("Original dictionary:", students_scores)
    print("Comprehension kode brugt:",
          "{navn: karakter for navn, karakter in students_scores.items() if karakter > 4}")
    print("Ny dictionary:", functions.ComprehensionDictStudent(students_scores))


def vis_merge():
    L1 = [1, 3, 2, 5, 4]
    L2 = [6, 7, 8, 9, 10]
    print("Original lister:", L1, L2)
    print("Ny merged list:", functions.merge(L1, L2))


def vis_range():
    L1 = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    print("Original list:", L1)
    print("Ny list:", functions.detect_ranges(L1))


def vis_enumerator():
    fagListe = ["Python", "BigData", "Serversideprogrammering"]

    print("Comprehension kode brugt:", "{i: fag for i, fag in enumerate(fagListe, start=1)}")
    ny_datastruktur = functions.enumeratorFag(fagListe)
    print("Ny datastruktur:", ny_datastruktur)
    print()

    for nummer, fag in ny_datastruktur.items():
        print(f"[{nummer}] {fag}")

    fagValg = input("Vælg et fag (vælg 1, 2 eller 3): ").strip()
    if fagValg.isdigit() and int(fagValg) in ny_datastruktur:
        print("Du valgte:", ny_datastruktur[int(fagValg)])
    else:
        print("Ugyldigt valg.")


def vis_menu():
    print("Vælg 1 for at se hvordan teksten er skrivet med ”argument separator”")
    print("Vælg 2 for at se hvordan teksten er skrivet med ”formatted string literal notation”")
    print("Vælg 3 for at se ”Docstring”")
    print("Vælg 4 for at se kontrolstruktur ”loop”")
    print("Vælg 5 for at se ”variable og datatyper”")
    print("Vælg 6 for at se ”datastruktur”")
    print("Vælg 7 for at se ”arithmetic operators”")
    print("Vælg 8 for at se ”operators”")
    print("Vælg 9 for at se ”closures”")
    print("Vælg 10 for at se ”Comprehension”")
    print("Vælg 11 for at se ”merge”")
    print("Vælg 12 for at se ”range”")
    print("Vælg 13 for at se ”enumerator”")
    print("Vælg 14 for at se ”aktivitetsdag”")

    valg = input("Indtast hvilken valg: ").strip()
    print()

    if valg == "1":
        ovelse2_1.argument_separator()
    elif valg == "2":
        ovelse2_1.formatted_string_literal()
    elif valg == "3":
        ovelse2_2.vis_docstring(__doc__)
    elif valg == "4":
        ovelse2_3.vis()
    elif valg == "5":
        ovelse2_4.vis()
    elif valg == "6":
        ovelse2_5.vis()
    elif valg == "7":
        ovelse2_6.vis()
    elif valg == "8":
        ovelse2_7.vis()
    elif valg == "9":
        ovelse2_8.vis()
    elif valg == "10":
        vis_comprehension()
    elif valg == "11":
        vis_merge()
    elif valg == "12":
        vis_range()
    elif valg == "13":
        vis_enumerator()
    elif valg == "14":
        aktivitetsdag.vis()
    else:
        print("Ugyldigt valg.")

    return valg


if __name__ == "__main__":
    vis_menu()
