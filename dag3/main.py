import csv
import os

from teacher import Teacher
from student import Student

DATA_FILE = "data.csv"

SUBJECTS = [
    "IoT_Embedded",
    "Python",
    "BigData_1",
    "Softwaresikkerhed_og_test",
    "Serversideprogrammering",
]

teachers = []
students = []


def ask_name(prompt):
    while True:
        name = input(prompt).strip()
        if name == "0":
            return None
        if name != "":
            return name
        print("Feltet må ikke være tomt.")


def choose(options, prompt):
    for i in range(len(options)):
        print("[" + str(i + 1) + "] " + options[i])

    while True:
        valg = input(prompt).strip()
        if valg == "0":
            return -1
        if valg.isdigit() and 1 <= int(valg) <= len(options):
            return int(valg) - 1
        print("Ugyldigt valg.")


def get_teacher_names():
    navne = []
    for teacher in teachers:
        navne.append(teacher.get_full_name())
    return navne


def load_data():
    if not os.path.exists(DATA_FILE):
        return

    with open(DATA_FILE, encoding="utf-8") as file:
        for row in csv.reader(file):
            if len(row) < 4:
                continue
            if row[0] == "teacher":
                if row[3] == "":
                    subjects = []
                else:
                    subjects = row[3].split("|")
                teachers.append(Teacher(row[1], row[2], subjects))
            else:
                students.append(Student(row[1], row[2], row[3]))


def save_data():
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for teacher in teachers:
            writer.writerow(teacher.to_row())
        for student in students:
            writer.writerow(student.to_row())


def show_all_teachers():
    print()
    print("List af alle lærer:")
    if len(teachers) == 0:
        print("(ingen lærere oprettet endnu)")
        return

    for teacher in teachers:
        print("- " + teacher.get_full_name() + ", fag:")
        for subject in teacher.get_subjects():
            elever = []
            for student in students:
                if student.get_subject() == subject:
                    elever.append(student)

            if len(elever) == 0:
                print("    - " + subject)
            else:
                print("    - " + subject + ", Elever:")
                for student in elever:
                    print("        - " + student.get_full_name())


def create_teacher():
    print()
    first_name = ask_name("Angiv lærens fornavn: ")
    if first_name is None:
        return

    last_name = ask_name("Angive lærens efternavn: ")
    if last_name is None:
        return

    print("Angive fag:")
    valg = choose(SUBJECTS, "Vælg et fag fra listen: ")
    if valg == -1:
        return

    teacher = Teacher(first_name, last_name, [SUBJECTS[valg]])
    teachers.append(teacher)

    print()
    print(teacher.get_full_name() + " er nu oprettet som lærer med følgende fag:")
    print(teacher.get_subjects_text())


def update_teacher():
    print()
    print("List af alle lærer:")
    if len(teachers) == 0:
        print("(ingen lærere oprettet endnu)")
        return

    valg = choose(get_teacher_names(), "Vælg en lærer fra listen: ")
    if valg == -1:
        return

    teacher = teachers[valg]
    print()
    print(teacher.describe())
    print()

    handlinger = [
        "Tilføj flere fag for " + teacher.get_full_name() + ".",
        "Slet et fag.",
        "Slet lærer " + teacher.get_full_name() + ".",
    ]
    valg = choose(handlinger, "Vælg 1, 2 eller 3: ")
    if valg == -1:
        return

    if valg == 0:
        print()
        print("Angiv fag:")
        fag = choose(SUBJECTS, "Vælg et fag fra listen: ")
        if fag == -1:
            return
        if teacher.has_subject(SUBJECTS[fag]):
            print()
            print("Læreren har allerede faget " + SUBJECTS[fag] + ".")
            return
        teacher.add_subject(SUBJECTS[fag])

    elif valg == 1:
        if len(teacher.get_subjects()) == 0:
            print()
            print("Læreren har ingen fag at slette.")
            return
        print()
        print("Angiv fag at slette:")
        fag = choose(teacher.get_subjects(), "Vælg fag fra listen: ")
        if fag == -1:
            return
        teacher.remove_subject(teacher.get_subjects()[fag])

    else:
        teachers.remove(teacher)
        print()
        print(teacher.get_full_name() + " er slettet.")
        return

    print()
    print(teacher.describe())


def add_student():
    print()
    first_name = ask_name("Angiv elevens fornavn: ")
    if first_name is None:
        return

    last_name = ask_name("Angiv elevens efternavn: ")
    if last_name is None:
        return

    valg = choose(SUBJECTS, "Vælg et fag fra listen: ")
    if valg == -1:
        return

    student = Student(first_name, last_name, SUBJECTS[valg])
    students.append(student)

    print()
    print(student.describe())


def show_menu():
    print()
    print("--------------------------------")
    print("[1] Vis list af alle lærer")
    print("[2] Opret lærer")
    print("[3] Opdater lærer")
    print("[4] Tilføj elev til fag")
    print("[5] SAVE and EXIT")


def main():
    load_data()

    while True:
        show_menu()
        valg = input("Vælg 1, 2, 3, 4 eller 5: ").strip()

        if valg == "1":
            show_all_teachers()
        elif valg == "2":
            create_teacher()
        elif valg == "3":
            update_teacher()
        elif valg == "4":
            add_student()
        elif valg == "5":
            save_data()
            break
        else:
            print("Ugyldigt valg.")


main()
