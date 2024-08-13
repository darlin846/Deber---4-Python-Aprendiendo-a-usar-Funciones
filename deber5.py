y = 10

def ModificarVariableGlobal():
    global y  
    y = y + 20
    print(f"variable global y modificarla es: {y}")

# Llamar a la función
ModificarVariableGlobal()

# Mostrar el valor de la variable global después de la modificación
print(f"variable global y es: {y}")