def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

resultadosuma, resultadoresta, resultadomultiplicacion = operaciones(8, 3)

print(f"suma: {resultadosuma}, resta: {resultadoresta}, multiplicacion: {resultadomultiplicacion}")