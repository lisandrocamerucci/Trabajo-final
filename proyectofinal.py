def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1 
        else:
            derecha = medio - 1

    return -1 

lista_ordenada = [1, 3, 5, 11, 22, 33, 45, 55, 76, 80, 89, 90]  
objetivo = int(input("Por favor ingrese tu objetivo: "))

resultado = busqueda_binaria(lista_ordenada, objetivo)

if resultado != -1:
    print(f"El número {objetivo} se encuentra en la posición {resultado}.")
else: 
    print(f"El número {objetivo} no se encuentra en la lista.")
