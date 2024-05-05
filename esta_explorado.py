def esta_explorado(t, inicio, fin):
    max_val = max(t[inicio:fin + 1])  # Encontrar el número más grande en el segmento
    max_index = t[inicio:fin + 1].index(max_val) + inicio  # Obtener el índice del número más grande
    t[inicio:max_index + 1] = [max_val] + t[inicio:max_index]  # Colocar el número más grande al principio
    return t

# Definir las variables fuera de la función menu
t = []
inicio = 0
fin = 0

def menu():
    global t, inicio, fin
    
    while True:
        print("Bienvenido a la ordenación por segmentos")
        print("Seleccione una opción:")
        print("1. Ingresar la lista de números separados por espacios")
        print("2. Seleccione el número donde desea que comience el primer segmento")
        print("3. Seleccione el número donde desea que termine el primer segmento")
        print("4. Realizar la exploración")
        print("5. Salir")
        
        opcion = int(input("Opción: "))
        
        if opcion == 1:
            t = list(map(int, input("Ingrese la lista de números separados por espacios: ").split()))
            print("")
        elif opcion == 2:
            inicio = int(input("Ingrese el índice de inicio del segmento: "))
            print("")
        elif opcion == 3:
            fin = int(input("Ingrese el índice de fin del segmento: "))
            print("")
        elif opcion == 4:
            resultado = esta_explorado(t, inicio, fin)
            print("Lista después de la exploración:", resultado)
            print("")
            break
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
