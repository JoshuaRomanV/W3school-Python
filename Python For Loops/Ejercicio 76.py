# En el bucle, cuando el valor del elemento es "banana", salta directamente al siguiente elemento.

frutas = ["manzana", "plátano", "cereza"]
for x in frutas:
    if x == "banana":
        continue
    print(x)