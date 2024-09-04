# Pide al usuario ingresar 7 números y muestra cuál es el mayor de ellos

numeros = []

for i in range(7):
    numero = int(input(f"Ingrese {i + 1}° numero: "))
    numeros.append(numero)

numero_mas_alto = numeros[0]

for numero in numeros:
    if numero > numero_mas_alto:
        numero_mas_alto = numero


print(f"El número más alto es el: {numero_mas_alto}")
