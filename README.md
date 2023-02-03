# Quiz 1 | 2223-2
## Problema 1 (4pts):
Con dos dados, al azar, se pueden obtener números entre 2 y 12 de varias formas. Crea un programa que reciba por teclado un número entre 2 y 12 y retorne las combinaciones posibles de números para que su suma sea igual al número ingresado (no debe repetirse la combinación, por ejemplo, 4-5 y 5-4 debe mostrarse solo una vez).

### Ejemplos de output:
```
> Combinaciones para 5:
   * 1-4
   * 2-3
```
```
 > Combinaciones para 9:
   * 3-6
   * 4-5
```


## Problema 2 (6pts):
Diseña un algoritmo que clasifique los números de la lista dada en las categorías del diccionario que se muestra a continuación:
```
numeros = [111, 15, 952, 7952, 74147, 994442, 0, 963214, 42, 1230, 778877, 95159, 23, 20, 1, 10, 122]

numeros_clasif = {
    "Palíndromos": [ ],
    "Con cifras repetidas": [ ]
}
```

### Output esperado:
Imprimir el diccionario con los números clasificados.
```
> { "Palíndromos": [111, 74147, 0, 778877, 95159, 1], "Con cifras repetidas": [111, 74147, 994442, 778877, 95159, 122] }
```

## Problema 3 (10pts):
OpenAI te ha contratado para que diseñes un software que gestione información referente a su modelo de inteligencia artificial GPT-3. A continuación, se muestra una lista con la información recolectada referente a los cinco datasets que la empresa usa para entrenar al modelo:
```
datasets = [
    { "Nombre": "Common Crawl", "Cantidad de tokens": 410000000000, "Tokens para set de entrenamiento (%)": 60 },
    { "Nombre": "WebText2", "Cantidad de tokens": 19000000000, "Tokens para set de entrenamiento (%)": 22 },
    { "Nombre": "Books 1", "Cantidad de tokens": 12000000000, "Tokens para set de entrenamiento (%)": 8 },
    { "Nombre": "Books 2", "Cantidad de tokens": 55000000000, "Tokens para set de entrenamiento (%)": 8 },
    { "Nombre": "Wikipedia", "Cantidad de tokens": 3000000000, "Tokens para set de entrenamiento (%)": 3 },
]
```
El software debe contar con estas funcionalidades:
- **Consultar datasets (2pt):** El software debe mostrar, de forma ordenada y amigable para el usuario, toda la información de los datasets de la lista, además de la cantidad de tokens de cada dataset usada para el entrenamiento del modelo (es decir, la cantidad total de tokens multiplicada por el porcentaje de tokens usados para el set de entrenamiento).

	***Ejemplo de output para un dataset:***
```
> -- Common Crawl ------
       Cantidad de tokens: 410000000000
       Porcentaje de tokens para set de entrenamiento: 60%
       Cantidad de tokens para set de entrenamiento: 246000000000.0
```


- **Modificar porcentajes (3pts):** El usuario debe poder modificar el porcentaje de tokens que el modelo usa para el set de entrenamiento. El usuario debe seleccionar el dataset que quiera modificar y actualizar el valor de "Tokens para set de entrenamiento (%)". **Dicho valor debe ser un número entero menor o igual que 75, y mayor o igual que 3.**

- **Estadísticas (2pts):** Se requiere que se muestren las siguientes estadísticas:
  - Cantidad total de tokens entre todos los datasets. (0.5)
  - Dataset con mayor porcentaje de tokens tomados para el set de entrenamiento. (0.75)
  - Dataset con menor porcentaje de tokens tomados para el set de entrenamiento. (0.75)

### REQUERIMIENTOS DEL ALGORITMO (3pts)

- Contar con un menú que permita al usuario seleccionar la acción a realizar.
- Volver al menú inicial al finalizar cada operación, y permitir al usuario cerrar el programa cuando lo desee.
- Tolerancia a ingresos inválidos: 
  - Validar todos los inputs numéricos.
  - Cualquier otro input utilizado debe ser tolerante a ingresos inválidos.
- Tomar en cuenta las convenciones de Python y buenas prácticas a la hora de programar.

## Bono (4pts):
Crea un algoritmo que retorne las coordenadas ([fila, columna]) del elemento que es diferente a los demás.

**Nota:** Las filas y columnas del output deben ser índice base 1 (es decir, si el elemento está en la posición [0,3], debe mostrarse al usuario como [1,4]).

### Inputs: (estas tres variables son con las que deben trabajar. No deben pedir nada por teclado ni inventar matrices nuevas)
```
matrix_1 = [ [ "+", "+", "-", "+"], [ "+", "+", "+", "+"], [ "+", "+", "+", "+"], [ "+", "+", "+", "+"] ]
matrix_2 = [ [ "a", "a", "a", "a", "a", "a"], [ "a", "a", "a", "a", "a", "a"], [ "a", "a", "a", "a", "z", "a"] ]
matrix_3 = [ [ "O", "O" ], [ "O", "X" ], [ "O", "O" ], [ "O", "O" ], [ "O", "O" ] ]
```

### Output esperado:
```
> [1, 3]
> [3, 5]
> [2, 2]
```
