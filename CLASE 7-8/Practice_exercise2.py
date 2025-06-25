# Ejercicio 2: Calculadora de estadisticas

def calcular_estadisticas(numeros):
    if len(numeros) == 0:
        return "La lista está vacia."
    estadisticas = {
        "suma": sum(numeros),
        "promedio": sum(numeros),
        "maximo": max(numeros),
        "minimo": min(numeros),
        "cantidad": len(numeros)
    }
    return estadisticas

#prueba de la funcion

numeros = (15, 25, 35, 45, 55, 65)

# Mostrar lista de forma vertical
print("Numeros en la lista:")
for numero in numeros:
    print(numero)

# Mostrar estadisticas
resultados = calcular_estadisticas(numeros)
print("\nEstadisticas:")
for clave, valor in resultados.items():
    print(f"{clave}: {valor}")    