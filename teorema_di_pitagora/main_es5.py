# <redacted>
# 02/04/2025
import math
base = int(input("Inserisci la base del triangolo: "))
altezza = int(input("Inserisci l'altezza del triangolo: "))
if base < 1 or altezza < 1:
    print("La base o l'altezza non sono validi")
else:
    ipotenusa = math.sqrt((base ** 2) + (altezza ** 2))
    print("L'ipotenusa è:", ipotenusa)
