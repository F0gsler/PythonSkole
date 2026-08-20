"""2.5 Datastruktur."""


def vis():
    frugter = ["Date", "Cherry", "Banana", "Apple"]
    print("1. Opretter en liste af frugter:")
    print(frugter)

    frugter.append("Elderberry")
    frugter.append("Fig")
    print("Tilføjer følgende frugter til listen: Elderberry og Fig:")
    print(frugter)

    print("Der er i alt: " + str(len(frugter)) + " frugter i listen.")

    frugter.remove("Cherry")
    print("Fjerner følgende frugt fra listen: Cherry:")
    print(frugter)

    print("Første og sidste frugt i listen:")
    print(frugter[0], frugter[-1])

    print("Udskriver alfabetisk sorteret liste:")
    print(sorted(frugter))


if __name__ == "__main__":
    vis()
