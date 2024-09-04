# Crea un programa que invierta el orden de un vector de 6 elementos.

vector = []

for i in range(6):
    valor = int(input(f"Ingrese el número {i+1}: "))
    vector.append(valor)

vector_invertido = vector[::-1]

print("\nLista invertida:")
print(vector_invertido)
