def busqueda_binaria(array, elemento, inicio, fin):
    """Realiza una búsqueda binaria en la lista array para encontrar la posición de inserción del elemento."""
    if inicio == fin:
        return inicio if array[inicio] > elemento else inicio + 1
    if inicio > fin:
        return inicio
    
    medio = (inicio + fin) // 2
    if array[medio] < elemento:
        return busqueda_binaria(array, elemento, medio + 1, fin)
    elif array[medio] > elemento:
        return busqueda_binaria(array, elemento, inicio, medio - 1)
    else:
        return medio

def ordenamiento_insercion_dicotomica(t):
    """Ordena la lista t en su lugar utilizando el algoritmo de inserción por dicotomía."""
    for i in range(1, len(t)):
        actual = t[i]
        posicion = busqueda_binaria(t, actual, 0, i - 1)
        
        # Desplazar elementos para hacer espacio para el elemento actual
        for j in range(i, posicion, -1):
            t[j] = t[j - 1]
        
        # Insertar el elemento actual en la posición correcta
        t[posicion] = actual

def menu():
    print("Bienvenido a la búsqueda dicotómica")
    print("Seleccione una opción:")
    print("1. Ingresar la lista de elementos desordenados")
    print("2. Ordenar la lista de elementos")
    print("3. Salir")
    opcion = int(input("Opción: "))
    
    return opcion

numeros = []

opcion = menu()
while opcion != 3:
    if opcion == 1:
        # Solicitar al usuario que ingrese los números
        numeros = input("Ingrese una serie de números separados por espacios: ").split()
        # Convertir los números ingresados a enteros
        numeros = [int(numero) for numero in numeros]
    elif opcion == 2:
        # Verificar si hay números ingresados
        if numeros:
            # Llamar a la función de ordenamiento e imprimir el resultado
            ordenamiento_insercion_dicotomica(numeros)
            print("Lista ordenada:", numeros)
            print("")
            break
        else:
            print("No ha ingresado ninguna lista de números.")
    opcion = menu()

while opcion == 3:
    print("Gracias por usar la búsqueda dicotómica.")
    break
    opcion = menu()
