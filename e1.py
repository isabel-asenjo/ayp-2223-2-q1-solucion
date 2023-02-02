num = int(input("Ingrese un numero entre 2 y 12: "))
while not num in range(2,13):
    num = int(input("Ingrese un numero entre 2 y 12: "))

combinaciones = []

for a in range(1, 7): # primer dado
    for b in range(1, 7): # segundo dado
        if a + b == num and not sorted((a, b)) in combinaciones: # se revisa si la suma entre el número obtenido en el primer dado y el obtenido en el segundo es igual al input, y además esa combinación no se ha guardado todavía
            combinaciones.append(sorted((a, b))) # se guarda la combinación nueva

print(f"Combinaciones para {num}:")
for c in combinaciones:
    print(f"* {c[0]}-{c[1]}")