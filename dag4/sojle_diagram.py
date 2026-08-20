import matplotlib.pyplot


def generer_soejle_diagram(labels, data, titel, x_tekst, y_tekst):
    matplotlib.pyplot.bar(labels, data)
    matplotlib.pyplot.title(titel)
    matplotlib.pyplot.xlabel(x_tekst)
    matplotlib.pyplot.ylabel(y_tekst)
    matplotlib.pyplot.show()