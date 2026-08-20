"""Grundlæggende Python programmering."""

import ovelse2_1
import ovelse2_2
import ovelse2_3
import ovelse2_4
import ovelse2_5
import ovelse2_6
import ovelse2_7
import ovelse2_8


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
    else:
        print("Ugyldigt valg.")

    return valg


if __name__ == "__main__":
    vis_menu()
