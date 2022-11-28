from sys import argv

"""
Pārbauda komandrindas argumentus.
Atgriež paziņojumu, ja skaits nav derīgs.
"""

def argumentu_parbaude() -> str:

    if len(argv) == 2:
        if argv[1].endswith(".txt"):
            return argv[1]
        else:
            return "Nederīgs faila nosaukums!"

    return "Nederīgs argumentu skaits!"  
