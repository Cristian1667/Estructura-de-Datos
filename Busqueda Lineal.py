# Crear una lista de números del 1 al 1000 (ordenada)
lista = list(range(1, 1001))

# Imprimir primeros y últimos elementos de la lista ordenada
print("Lista ordenada:")
print("Primeros 10 elementos:", lista[:10])
print("Últimos 10 elementos:", lista[-10:])

# Función de búsqueda lineal con contador
def linear_search(arr, target):
    contador = 0  # Contador de iteraciones
    for index, num in enumerate(arr):
        contador += 1  # Incrementar contador en cada iteración
        if num == target:
            print(f"\nNúmero encontrado después de {contador} iteraciones.")
            return index  # Retornar el índice del elemento encontrado
    print(f"\nNúmero no encontrado después de {contador} iteraciones.")
    return -1  # Retornar -1 si el elemento no se encuentra

# Buscar un número en la lista ordenada
target = 50  # Número a buscar
index = linear_search(lista, target)  # Buscar el número

if index != -1:
    print(f"El número {target} se encuentra en el índice {index} (en lista ordenada).")
else:
    print(f"El número {target} no se encuentra en la lista.")
