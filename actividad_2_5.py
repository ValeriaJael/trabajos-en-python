nombres=["a"]
opcion= int(input("Para añadir un nombre escriba 1, para eliminar un nombre escriba 2, para ordenar la lista escriba 3, para buscar un nombre pulse 4, para mostrar la lista completa pulse 5, para salir del programa, pulse 6 : "))
while opcion<7:
    if opcion == 1:
        nombre_agregado = input("Añada el nombre: ")
        nombres.append(nombre_agregado)
    elif opcion == 2:
        print (f"La lista de nombres es {nombres}")
        eliminar=input("Elija que nombre desea eliminar: ")
        nombres.remove(eliminar)
    elif opcion== 3: 
        nombres.sort()
        print (nombres)
    elif opcion == 4:
        nombre_buscar = input("Cual es el nombre que desea buscar? ")
        if nombre_buscar in nombres:
            print ("El nombre que busca, si está en la lista")
        else:
            print ("El nombre que busca NO está en la lista")
    elif opcion == 5:
        print (f"La lista completa es: {nombres}")
    elif opcion == 6:
        print ("Operación terminada")
        break
    opcion= int(input("Para añadir un nombre escriba 1, para eliminar un nombre escriba 2, para ordenar la lista escriba 3, para buscar un nombre pulse 4, para mostrar la lista completa pulse 5, para salir del programa, pulse 6 : "))