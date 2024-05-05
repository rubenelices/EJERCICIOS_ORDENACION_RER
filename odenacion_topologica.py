from collections import deque

def topological_sort(n, constraints):
    # Construir el grafo
    adj_list = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}
    
    for i, j in constraints:
        adj_list[i].append(j)
        in_degree[j] += 1

    # Cola para mantener todos los nodos sin dependencias entrantes
    queue = deque([i for i in in_degree if in_degree[i] == 0])
    top_order = []

    # Proceso de eliminación de nodos
    while queue:
        node = queue.popleft()
        top_order.append(node)
        for adjacent in adj_list[node]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    # Si el tamaño de top_order es diferente de n, entonces hay un ciclo
    if len(top_order) != n:
        return "No es posible realizar una ordenación topológica debido a un ciclo, revisa si hay algun par de restricciones que se contradigan"
    return top_order

def menu():
    print("Bienvenido al programa de ordenación topológica")
    n = int(input("Ingrese el número de tareas: "))
    constraints = []
    print("Ingrese las restricciones entre las tareas (ingrese '0 0' para terminar)")
    while True:
        i, j = map(int, input("Restricción (i j): ").split())
        if i == 0 and j == 0:
            break
        if i < 1 or i > n or j < 1 or j > n:
            print("Las tareas deben estar en el rango de 1 a", n)
            continue
        constraints.append((i, j))
    
    print("Orden topológico de las tareas:", topological_sort(n, constraints))

# Ejecutar el menú
menu()

