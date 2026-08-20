"""Funktioner til datastruktur begreberne: comprehension, merge, range og enumerator."""


def ComprehensionListNum(numbersList):
    comp_sqrList = [i ** 2 for i in numbersList]
    return comp_sqrList


def ComprehensionListStr(stringsList):
    comp_stringsList = [s for s in stringsList if len(s) > 3]
    return comp_stringsList


def ComprehensionSetsNum(numbersSets):
    comp_evenSets = {i for i in numbersSets if i % 2 == 0}
    return comp_evenSets


def ComprehensionSetsStr(wordsSets):
    comp_WordsSets = {word[0] for word in wordsSets}
    return comp_WordsSets


def ComprehensionDictKeysValues(keys, values):
    ny_dict = {k: v for k, v in zip(keys, values)}
    return ny_dict


def ComprehensionDictStudent(students_scores):
    ny_dict = {navn: karakter for navn, karakter in students_scores.items() if karakter > 4}
    return ny_dict


def merge(L1, L2):
    L3 = sorted(L1 + L2)
    return L3


def detect_ranges(L1):
    sorteret = sorted(L1)
    grupper = []
    aktuel = [sorteret[0]]

    for tal in sorteret[1:]:
        if tal == aktuel[-1] + 1:
            aktuel.append(tal)
        else:
            grupper.append(aktuel)
            aktuel = [tal]
    grupper.append(aktuel)

    resultat = []
    for gruppe in grupper:
        if len(gruppe) == 1:
            resultat.append(gruppe[0])
        else:
            resultat.append(f"({gruppe[0]}-{gruppe[-1]})")
    return resultat


def enumeratorFag(fagListe):
    ny_dict = {i: fag for i, fag in enumerate(fagListe, start=1)}
    return ny_dict
