# Ejercicio 1: Funciones de saludo personalizado
def saludar_persona(nombre, hora):
    if hora < 12:
        return f"¡Buenos días, {nombre}!"
    elif hora < 18:
        return f"¡Buenas tardes, {nombre}!"
    else:
        return f"¡Buenas noches, {nombre}!"
    
# prueba de la funcion
print(saludar_persona("Natalia", 8))
print(saludar_persona("Marcela", 13))
print(saludar_persona("Andres", 22))  