numeros = []

for i in range(0, 10):
    numero = float(input(f"Ingrese {i + 1}° numero: "))

    numeros.append(numero)

promedio =  sum(numeros) / len(numeros)
print(promedio)