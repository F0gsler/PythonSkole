"""main.py - kører koden fra ovelse.py."""

import ovelse

valg = ovelse.vis_menu()

if valg == "3":
    print(ovelse.__doc__)
