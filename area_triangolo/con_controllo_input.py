# <redacted>
# 02/04/2025
base = int(input("Inserisci la base del triangolo (in cm): "))
altezza = int(input("Inserisci l'altezza del triangolo (in cm): "))
if base < 1 or altezza < 1:
    print("Hai inserito un'altezza o una base non valida")
else:
    area = (base * altezza) / 2
    print("L'area del triangolo è", area, "cm quadrati")
