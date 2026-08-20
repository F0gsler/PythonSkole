"""2.6 Arithmetic operators."""

import math


def andengradsligning(a, b, c):
    diskriminant = math.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + diskriminant) / (2 * a)
    x2 = (-b - diskriminant) / (2 * a)
    return (x1, x2)


def vis():
    a = 1
    b = -3
    c = 2

    resultater = andengradsligning(a, b, c)

    print("x = (-b +/- sqrt(b**2 - 4*a*c)) / (2*a)")
    print("a =", a, " b =", b, " c =", c)
    print("Resultaterne gemmes i en tuple, fordi en tuple ikke kan overskrives:")
    print(resultater)
    print("x1 =", resultater[0])
    print("x2 =", resultater[1])


if __name__ == "__main__":
    vis()
