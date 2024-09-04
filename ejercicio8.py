# 3. Pide al usuario llenar una matriz de 2x3 y muestra su transpuesta.

filas = 2
columnas = 3

matriz =[]

for i in range(filas):
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"ingrese el valor de la posicion ({i + 1}, {j + 1}): "))
            fila.append(valor)
            matriz.append(fila)

print("\nMatriz Original:")

for fila in matriz:
    print(fila)

transpuesta = []
for j in range(columnas):
    fila_transpuesta = []
    for i in range(filas):
        fila_transpuesta.append(matriz[i][j])
    transpuesta.append(fila_transpuesta)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)