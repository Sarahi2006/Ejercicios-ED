# Genera una matriz identidad de tamaño 4x4.
filas = 4
columnas = 4

matriz = []



for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para la posicion ({i + 1}, {j + 1}): "))
        fila.append(valor)
        matriz.append(fila)

print("La matriz es:")
for fila in matriz:
    print(fila)