C som dit primære sprog er **IronPython** det naturlige valg.

Fordele ved IronPython til dig:

- **Direkte .NET-integration** – du kan importere og bruge dine egne C#-klasser og .NET-biblioteker direkte fra Python-kode, og omvendt kalde Python-kode fra C#.
- **Fælles CLR-runtime** – ingen behov for interop-lag, sockets eller separate processer; alt kører i samme .NET-proces.
- **Deler objekter på tværs** – du kan sende .NET-objekter frem og tilbage mellem C# og Python uden serialisering.
- **Python 3-support** – fra IronPython 3.4 er der god understøttelse af moderne Python 3-syntaks.

**Typiske use cases for dig som C#-udvikler:**

- Scripting-lag i en C#-applikation (f.eks. lade brugere skrive Python-plugins/makroer til dit program)
- Automatisere eller teste .NET-kode med Python's mere fleksible syntaks
- Prototyping af logik i Python, som senere kaldes fra din C#-kodebase

**Én ting at være opmærksom på:** IronPython har ikke adgang til CPython's C-extension-moduler (som NumPy, Pandas med C-bindings osv.), fordi det ikke kører på CPython's C-API. Hvis du har brug for tunge data science-biblioteker sammen med .NET-integration, er alternativet at køre almindelig CPython som en separat proces og kommunikere via f.eks. gRPC, pipes eller REST – lidt mere arbejde, men du får fuld adgang til hele Python-økosystemet.

### 1.3 notes Python
1. hver vm 
2. Nej