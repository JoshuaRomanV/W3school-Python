# En el ciclo, cuando i es 3, salta directamente a la siguiente iteración.

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)