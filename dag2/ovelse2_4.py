"""2.4 Variable og datatyper."""

import base64


def simple_type():
    print("Simple type:")
    a = 1
    b = "Hello, World!"
    c = True
    d = 1.123
    print("a is of type", type(a))
    print("b is of type", type(b))
    print("c is of type", type(c))
    print("d is of type", type(d))


def complex_type():
    print("Complex type:")
    c = 0 + 2j
    print("c * c =", c * c)
    print("c / c =", c / c)


def binary_type():
    print("Binary types:")
    tekst = "Hello, World!"
    data = tekst.encode("utf-8")

    print("Hexadecimal:", data.hex())

    decimal = []
    for byte in data:
        decimal.append(str(byte))
    print("Decimal:", " ".join(decimal))

    binaer = []
    for byte in data:
        binaer.append(format(byte, "08b"))
    print("Binary:", " ".join(binaer))

    oktal = []
    for byte in data:
        oktal.append(format(byte, "03o"))
    print("Octal:", " ".join(oktal))

    print("Base64:", base64.b64encode(data).decode("utf-8"))

    unicode_tegn = []
    for tegn in tekst:
        unicode_tegn.append("U+" + format(ord(tegn), "04X"))
    print("Unicode:", " ".join(unicode_tegn))


def vis():
    simple_type()
    print()
    complex_type()
    print()
    binary_type()


if __name__ == "__main__":
    vis()
