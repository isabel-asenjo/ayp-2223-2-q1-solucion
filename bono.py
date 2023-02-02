matrix_1 = [ [ "+", "+", "-", "+"], [ "+", "+", "+", "+"], [ "+", "+", "+", "+"], [ "+", "+", "+", "+"] ]
matrix_2 = [ [ "a", "a", "a", "a", "a", "a"], [ "a", "a", "a", "a", "a", "a"], [ "a", "a", "a", "a", "z", "a"] ]
matrix_3 = [ [ "O", "O" ], [ "O", "X" ], [ "O", "O" ], [ "O", "O" ], [ "O", "O" ] ]

matrices = [matrix_1, matrix_2, matrix_3]

for matrix in matrices:
    different = [] # esta lista va a guardar las coordenadas del elemento que es distinto
    for i in range(len(matrix)): # itero sobre cada fila de la matriz (o cada lista dentro de la lista grande)
        if len(set(matrix[i])) != 1: # con el set verifico si quitando todos los elementos repetidos de la lista actual me quedan uno o dos. Si me quedan dos, conseguí la lista que tiene al elemento diferente
            for j in range(len(matrix[i])): # itero sobre esa lista para conseguir la segunda coordenada
                if matrix[i].count(matrix[i][j]) == 1: # reviso cuántas veces se repite el elemento actual en la lista. Si está solo una vez, conseguí el elemento diferente
                    different = [i+1, j+1] # guardo sus coordenadas

    print(different)