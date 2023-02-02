numeros = [111, 15, 952, 7952, 74147, 994442, 0, 963214, 42, 1230, 778877, 95159, 23, 20, 1, 10, 122]
numeros_clasif = {
    "Palíndromos": [ ],
    "Con cifras repetidas": [ ]
}

for n in numeros: # reviso cada número de la lista
    if str(n) == str(n)[::-1]: # si ese número como string es igual a eso mismo pero volteado (usando el split), es palíndromo
        numeros_clasif["Palíndromos"].append(n) # guardo el número en la lista de palíndromos que está en el diccionario
    for cifra in str(n): # reviso cada cifra del número actual
        if str(n).count(cifra) > 1: # cuento cuántas repeticiones hay de dicha cifra. si hay más de una, la cifra está repetida
            numeros_clasif["Con cifras repetidas"].append(n) # guardo el número en la lista de números con cifras repetidas que está en el diccionario
            break # rompo el loop de la línea 10 porque ya conseguí por lo menos una cifra que se repite, y por lo tanto hace que ya pueda guardar al número en la lista. sin el break, el número se guardaría tantas veces como cifras repetidas haya (si tengo 998877, se guardaría 6 veces, porque hay tres cifras repetidas y cada cifra se repite dos veces)


print(numeros_clasif)