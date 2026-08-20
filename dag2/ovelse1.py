"""ovelse1.py - importerer og kører alle øvelser i en sammenhængende sekvens."""

import hello_world
import ovelse2_1
import ovelse2_2
import ovelse2_3
import ovelse2_4
import ovelse2_5
import ovelse2_6
import ovelse2_7
import ovelse2_8
import ovelse


def koer_alle():
    hello_world.hello_world()

    ovelse2_1.vis()
    print()
    ovelse2_2.vis()
    print()
    ovelse2_3.vis()
    print()
    ovelse2_4.vis()
    print()
    ovelse2_5.vis()
    print()
    ovelse2_6.vis()
    print()
    ovelse2_8.vis()
    print()
    ovelse.vis_comprehension()
    print()
    ovelse.vis_merge()
    print()
    ovelse.vis_range()
    print()
    ovelse.vis_enumerator()
    print()

    try:
        ovelse2_7.vis()
    except SystemExit:
        print("Lommeregneren blev afsluttet.")


if __name__ == "__main__":
    koer_alle()
