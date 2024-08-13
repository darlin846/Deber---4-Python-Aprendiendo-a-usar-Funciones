def funcionexterior():
    
    def funcioninterior(mensaje):
        print(f"mensaje es: {mensaje}")
    
    funcioninterior("función interior!")

funcionexterior()