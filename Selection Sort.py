# Programa Python para la implementación de Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Suponga que la posición actual se mantiene el elemento mínimo
        min_idx = i
        
        # Iterar a través de la parte no ordenada para encontrar el mínimo real
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Actualizar min_idx si se encuentra un elemento más pequeño
                min_idx = j
        
        # Mueve el elemento mínimo a su posición correcta
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print_array(arr)
