# 5. Solicita una matriz cuadrada de tamaño 3x3 y muestra los elementos de su
# diagonal principal.

matriz = []

print("Ingrese los valores para la matriz 3x3:")
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Posición ({i+1}, {j+1}): "))
        fila.append(valor)
    matriz.append(fila)

diagonal_principal = []

for i in range(3):
    diagonal_principal.append(matriz[i][i])

print("\nElementos de la diagonal principal:")
for elemento in diagonal_principal:
    print(elemento)
