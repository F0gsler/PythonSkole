"""Grundlæggende Python programmering."""
"""Grundlæggende Python programmering."""


import math
import base64



def argumentSeparator():
    """Marius"""

    print("Vælg 1 for at se hvordan teksten er skrivet med ”argument separator”")
    print("Vælg 2 for at se hvordan teksten er skrivet med ”formatted string literal notation”")
    print("vælg 3 for docstring")
    print("vælg 4 for loop")
    print("Vælg 5 for at se ”variable og datatyper”")
    print("Vælg 6 for at se ”datastruktur”")
    print("Vælg 7 for at se ”arithmetic operators”")
    print("Vælg 8 for at se ”operators”")
    print("Vælg 9 for at se ”closures”")


    valg = input("Indtast hvilken valg: ")

    if valg == "1":
        print("1", "plus", "1", "equals", "2")
    elif valg == "2":
        txt = f"1 plus 1 equals 2"
        print(txt)
    elif valg == "3":
        print(argumentSeparator.__doc__)   
    elif valg == "4":
        hej = ["Hello", "Hello", "Hello", "Bye!"]
        for f in  hej:
            print(f)

        i = 0    
        while i < len(hej):
            print(hej[i])
            i += 1

        L1 = [1,2,3,4,5,6,7,8,9,10]
        L2 = [1,2,3,4,5,6,7,8,9,10]

        for l in L1:
            for h in L2:
                print(f"{l * h:4}", end="")
            print()
    elif valg == "5":
        print("Simple Type")
        a = 1
        b = "hello world"
        c = True
        d = 1.123
        print("a is type of ", type(a))
        print("b is type of ", type(b))
        print("c is type of ", type(c))
        print("d is type of ", type(d))

        print("Complex Type")
        c = 0+2j
        print(c * c)
        print(c/c)

        print("Binary Type")
        text = "Hello, World!"
        data = text.encode()
        

        print(data.hex())

        print(list(data))

        print(bin(int(data.hex(), 16)))

        print(oct(int(data.hex(), 16)))

        print(base64.b64encode(data))
        
    elif valg == "6":
        i = ["Date", "Cherry", "Banana", "Apple"]
        print(f"Der er i alt: {i} frugter i listen. ")
        i.append("Elderberry")
        i.append("Fig")
        print(f"Der er i alt: {i} frugter i listen. ")
        i.pop(1)
        print(f": Fjerner følgende frugt fra listen: Cherry. {i}")
        
        print(i[0],"",i[-1])

        i.sort()
        print(i)
    elif valg == "7":
        a = 1
        b = -3
        c = 2
        x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        print(x)
    elif valg == "8":
        while True:

            print("1: Addition")
            print("2: Subtraktion")
            print("3: Multiplikation")
            print("4: Division")
            print("5: Afslut")
            valg = input("Vælg Operation(1-5): ")
            if valg == '5':
                break
            a = float(input("Indtast første tal: "))
            b = float(input("Indtast andet tal: "))


        
            if valg == '1':
                resultat = a + b
                operators = "-"
                print(f"Resultat: {a} {operators} {b} = {resultat}")
            elif valg == '2':
                resultat = a - b
                operators = "-"
                print(f"Resultat: {a} {operators} {b} = {resultat}")
            elif valg == '3':
                resultat = a * b
                operators = "-"
                print(f"Resultat: {a} {operators} {b} = {resultat}")
            elif valg == '4':
                resultat = a / b
                operators = "-"
                print(f"Resultat: {a} {operators} {b} = {resultat}")
    elif valg == "9":
        def opret_rabatberegner(rabat_procent):
            def beregn_pris(pris):
                return pris - (pris * rabat_procent / 100)
            return beregn_pris

        rabat10 = opret_rabatberegner(10)
        rabat25 = opret_rabatberegner(25)

        print(rabat10(500))
        print(rabat25(500))