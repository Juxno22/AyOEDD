def busqueda_binaria(array, elemento, izquierda, derecha):
    # Caso base: el elemento no está presente
    if izquierda > derecha:
        return -1

    # Encontrar el punto medio
    medio = izquierda + (derecha - izquierda) // 2

    # Si el elemento está en el medio
    if array[medio] == elemento:
        return medio

    # Si el elemento es menor que el medio, buscar en el subarray izquierdo
    elif array[medio] > elemento:
        return busqueda_binaria(array, elemento, izquierda, medio - 1)

    # Si el elemento es mayor, buscar en el subarray derecho
    else:
        return busqueda_binaria(array, elemento, medio + 1, derecha)

# Ordenamiento por selección
def ordenamiento_seleccion(array):
    n = len(array)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        # Intercambiar el elemento más pequeño con el primer elemento no ordenado
        array[i], array[min_idx] = array[min_idx], array[i]

# Ordenamiento burbuja
def ordenamiento_burbuja(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Ordenamiento quicksort recursivo
def quicksort(array, bajo, alto):
    if bajo < alto:
        # Dividir el array
        pi = particion(array, bajo, alto)
        # Ordenar las dos mitades
        quicksort(array, bajo, pi - 1)
        quicksort(array, pi + 1, alto)

# Función auxiliar para dividir el array para quicksort
def particion(array, bajo, alto):
    pivote = array[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if array[j] < pivote:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[alto] = array[alto], array[i + 1]
    return i + 1

# Función principal
if __name__ == "__main__":
    array = [12, 35, 1, 10, 34, 1]

    # Ordenar por selección
    array_seleccion = array.copy()
    ordenamiento_seleccion(array_seleccion)
    print("Ordenado por selección:", array_seleccion)

    # Ordenar por burbuja
    array_burbuja = array.copy()
    ordenamiento_burbuja(array_burbuja)
    print("Ordenado por burbuja:", array_burbuja)

    # Ordenar por quicksort
    array_quicksort = array.copy()
    quicksort(array_quicksort, 0, len(array_quicksort) - 1)
    print("Ordenado por quicksort:", array_quicksort)

    # Búsqueda binaria en el array ordenado
    elemento = 10
    resultado = busqueda_binaria(array_quicksort, elemento, 0, len(array_quicksort) - 1)
    if resultado == -1:
        print(f"Elemento {elemento} no encontrado.")
    else:
        print(f"Elemento {elemento} encontrado en la posición: {resultado}")
