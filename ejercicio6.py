# Solicita al usuario llenar una matriz de 3x3 y calcula la suma de todos sus
# elementos

matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese el número para la posición ({i+1}, {j+1}): "))
        fila.append(valor)
    matriz.append(fila)

suma = 0

for fila in matriz:
    for numero in fila:
        suma += numero

print("\nLa suma de todos los elementos es:", suma)
