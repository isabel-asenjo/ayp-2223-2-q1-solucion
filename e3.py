datasets = [
    { "Nombre": "Common Crawl", "Cantidad de tokens": 410000000000, "Tokens para set de entrenamiento (%)": 60 },
    { "Nombre": "WebText2", "Cantidad de tokens": 19000000000, "Tokens para set de entrenamiento (%)": 22 },
    { "Nombre": "Books 1", "Cantidad de tokens": 12000000000, "Tokens para set de entrenamiento (%)": 8 },
    { "Nombre": "Books 2", "Cantidad de tokens": 55000000000, "Tokens para set de entrenamiento (%)": 8 },
    { "Nombre": "Wikipedia", "Cantidad de tokens": 3000000000, "Tokens para set de entrenamiento (%)": 3 },
]


while True:
    print("Bienvenido al gestor de información de GPT-3\n1. Ver datasets\n2. Modificar porcentajes\n3. Estadísticas\n4. Salir")
    option = input("Ingrese una opción: ")
    print()
    if option == "1":
        print("DATASETS\n")

        # se muestran los datasets disponibles
        for i, dataset in enumerate(datasets):
            print(f"-- {dataset['Nombre']} ------")
            print(f"\tCantidad de tokens: {dataset['Cantidad de tokens']}")
            print(f"\tPorcentaje de tokens para set de entrenamiento: {dataset['Tokens para set de entrenamiento (%)']}%")
            print(f"\tCantidad de tokens para set de entrenamiento: {dataset['Cantidad de tokens'] * dataset['Tokens para set de entrenamiento (%)']/100}")

    elif option == "2":
        print("MODIFICACIÓN DE PORCENTAJES\n")

        # se muestran los datasets disponibles
        for i, dataset in enumerate(datasets):
            print(f"{i+1}. {dataset['Nombre']}")
        
        # se pregunta qué dataset se quiere consultar
        d = input("Ingrese el número correspondiente al dataset a consultar: ")
        while not d.isnumeric() or not int(d) in range(1, len(datasets) + 1):
            d = input("Opción inválida. Intente nuevamente: ")

        # se pide el porcentaje nuevo
        new_percentage = input("Ingrese el nuevo porcentaje de tokens para el set de entrenamiento: ")
        while not new_percentage.isnumeric() or int(new_percentage) not in range(3,76):
            new_percentage = input("Ingreso inválido. Intente otra vez: ")
        
        # se actualiza el valor en el diccionario
        datasets[int(d)-1]["Tokens para set de entrenamiento (%)"] = int(new_percentage)

        print("\nValor actualizado exitosamente!")

    elif option == "3":
        print("ESTADÍSTICAS\n")
        # variables
        total_tokens = 0
        biggest_percentage = ["", 2]
        smallest_percentage = ["", 76]
        train_set_tokens = 0

        # se itera sobre la lista de datasets
        for dataset in datasets:

            # se va acumulando la cantidad de tokens
            total_tokens += dataset["Cantidad de tokens"]

            # se revisa si el porcentaje del token actual es mayor que el registrado como mayor y que el registrado como menor, y se actualiza la variable en caso de que se cumpla alguna de las condiciones
            if biggest_percentage[1] < dataset["Tokens para set de entrenamiento (%)"]:
                biggest_percentage = [dataset["Nombre"], dataset["Tokens para set de entrenamiento (%)"]]
            if smallest_percentage[1] > dataset["Tokens para set de entrenamiento (%)"]:
                smallest_percentage = [dataset["Nombre"], dataset["Tokens para set de entrenamiento (%)"]]

            # se va acumulando la cantidad de tokens usados para el set de entrenamiento de cada dataset. luego se sacará el promedio dividiendo entre la cantidad de datasets
            train_set_tokens += dataset["Cantidad de tokens"] * (dataset["Tokens para set de entrenamiento (%)"] / 100)
        
        print("Cantidad total de tokens:", total_tokens)
        print("Dataset con mayor porcentaje de tokens para set de entrenamiento:", biggest_percentage[0])
        print("Dataset con menor porcentaje de tokens para set de entrenamiento:", smallest_percentage[0])
        print("Promedio de tokens usados para el set de entrenamiento:", train_set_tokens/len(datasets))

    elif option == "4":
        print("Hasta pronto!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
    print()