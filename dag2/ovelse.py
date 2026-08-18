"""Grundlæggende Python programmering."""


import math
import base64
import functions



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
    print("Vælg 10 for at se ”Comprehension”")
    print("Vælg 11 for merge")
    print("Vælg 12 for range")


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
                operators = "+"
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
    elif valg == "10":
        numbersList = [1, 2, 3, 4, 5] 
        stringsList =["apple", "an", "banana", "cat", "dog","elephant"]
        
        numbersSets = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 
        wordsSets = {"apple", "banana", "cherry", "date", "grapefruit", "fig", "grape"}

        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        students_scores = {"Thomas": 2,"Alex": 12, "Charlie": 10, "David": 4}

   

        ny_list = functions.ComprehensionListNum(numbersList)

        print(" # Comprehension: ", ny_list)
        print("Original list: ", numbersList)
        print("Comprehension kode brugt: ", "[i**2 for i in numbers]")

        print("Ny list: ", ny_list)

        ny_list = functions.ComprehensionListStr(stringsList)

        print("# Comprehension: ", ny_list)
        print("Original list: ", stringsList)
        print("Comprehension kode brugt: ", "[s for s in strings if len(s) > 3]")

        print("Ny list: ", ny_list)

        """Sets"""
        ny_Sets = functions.ComprehensionSetsNum(numbersSets)
        print("# Comprehension: ", ny_Sets)
        print("Original sets: ", numbersSets)
        print("Comprehension kode brugt: ", "comp_evenSets = {i for i in numbersSets if i % 2 == 0}")
        
        print("Ny list: ", ny_Sets)
        


        ny_Sets = functions.ComprehensionSetsStr(wordsSets)

        print("# Comprehension: ", ny_Sets)
        print("Original Sets: ", wordsSets)
        print("Comprehension kode brugt: ", "comp_WordsSets = [word[0] for word in wordsSets]")
        
        print("Ny list: ", ny_Sets)

        """Dict"""         
        ny_dict = functions.ComprehensionDictKeysValues(keys, values)



        print("# Comprehension: ", ny_dict)
        print(f"Original lister: keys={keys}, values={values}")
        print("Comprehension kode brugt: ", "ny_dict = {k: v for k, v in zip(keys, values)}")
        print("Ny list: ", ny_dict)
                
        ny_dict = functions.ComprehensionDictStudent(students_scores)
 
        print("# Comprehension: ", ny_dict)
        print(f"Original dictionary: {students_scores}")
        print("Comprehension kode brugt: ", "ny_dict = {navn: karakter for navn, karakter in students_scores.items() if karakter > 4}")
        print("Ny dictionary: ", ny_dict)  
    elif valg == "11":
        L1 = [1, 3, 2, 5, 4] 
        L2 = [6, 7, 8, 9, 10]
        new_merge = functions.merge(L1,L2)
        print("Ny Merge Liste: ", new_merge)
    elif valg == "12":
        L1 = [2,5,4,8,12,6,7,10,13]
        new_range = functions.detect_ranges(L1)
        print("Ny liste: ", new_range)
