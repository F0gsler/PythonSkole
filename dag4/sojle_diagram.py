from matplotlib import pyplot as plt


def generer_soejle_diagram(labels, data, titel, x_tekst, y_tekst):
    plt.bar(labels, data)
    plt.title(titel)
    plt.xlabel(x_tekst)
    plt.ylabel(y_tekst)
    plt.show()