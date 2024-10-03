def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es: {factorial_iterativo(numero)}")
