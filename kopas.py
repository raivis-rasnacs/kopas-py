# --- Uzvārds, klase ---

from argumenti import argumentu_parbaude
from ielasa_failu import ielasa_failu as ielasa_f
from aprekins import videjais

arg = argumentu_parbaude()

# pārtrauc programmas izpildi, ja arguments nav derīgs
if not arg.endswith(".txt"):
    print(arg)
    exit()

vertibas = ielasa_f(arg)

print(videjais(vertibas))
