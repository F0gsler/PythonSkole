"""2.3 Kontrol struktur."""


def for_loop():
    print("for loop:")
    for gang in range(3):
        print("Hello")
    print("Bye!")


def while_loop():
    print("while loop:")
    i = 0
    while i < 3:
        print("Hello")
        i = i + 1
    print("Bye!")


def indlejret_loop():
    print("Inlejrede loop:")
    L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for tal1 in L1:
        for tal2 in L2:
            print(f"{tal1 * tal2:4}", end="")
        print()


def vis():
    for_loop()
    print()
    while_loop()
    print()
    indlejret_loop()


if __name__ == "__main__":
    vis()
