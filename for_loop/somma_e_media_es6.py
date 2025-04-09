# <redacted>
# 09/04/2025
# Somma e media di n numeri
somma = 0
quantita = int(input("Quanti numeri vuoi inserire: "))
for i in range(quantita):
    somma += int(input("Inserisci il " + str((i + 1)) + "°" + " numero: "))
media = round(somma / quantita, 2)
print("La somma dei numeri è:", somma)
print("La media dei numeri è:", media)
