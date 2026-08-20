"""2.1 Grundlæggende input/output funktion."""


def argument_separator():
    print("1", "plus", "1", "equals", "2")
    print("Koden til punkt 1:")
    print('print("1", "plus", "1", "equals", "2")')


def formatted_string_literal():
    a = 1
    b = 1
    tekst = f"{a} plus {b} equals {a + b}"
    print(tekst)
    print("Koden til punkt 3:")
    print('tekst = f"{a} plus {b} equals {a + b}"')
    print("print(tekst)")


def vis():
    argument_separator()
    print()
    formatted_string_literal()


if __name__ == "__main__":
    vis()
