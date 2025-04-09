# <redacted>
# 09/04/2025
# Dati 10 numeri interi in input, calcolare la somma dei  quadrati dei numeri compresi tra 5 e 10
import math
somma = 0
for i in range(10):
    num = int(input("Inserisci un numero: "))
    if num >= 5 and num <= 10:
        somma += math.pow(num, 2)
print("La somma dei quadrati dei numeri compresi tra 5 e 10 è:", somma)
