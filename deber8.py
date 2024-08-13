def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Calcular el factorial 7
resultado_factorial = factorial(7)

print(f"El factorial de 7 es: {resultado_factorial}")