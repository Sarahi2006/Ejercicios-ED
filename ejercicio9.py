# 4. Realiza la multiplicación de dos matrices de 2x2. Solicita los datos para ambas
# matrices y muestra el resultado.

matriz1 = []
matriz2 = []

print("Ingrese los valores para la primera matriz:")
for i in range(2):  
    fila = []  
    for j in range(2): 
        valor = int(input(f"Posición ({i+1}, {j+1}): "))
        fila.append(valor)  
    matriz1.append(fila)  

print("\nIngrese los valores para la segunda matriz:")
for i in range(2):  
    fila = [] 
    for j in range(2):  
        valor = int(input(f"Posición ({i+1}, {j+1}): "))
        fila.append(valor) 
    matriz2.append(fila)  

resultado = []

for i in range(2):  
    fila_resultado = [] 
    for j in range(2): 
        suma = 0  
        for k in range(2): 
            suma += matriz1[i][k] * matriz2[k][j]  
        fila_resultado.append(suma) 
    resultado.append(fila_resultado)  

print("\nResultado de la multiplicación:")
for fila in resultado:
    print(fila)
