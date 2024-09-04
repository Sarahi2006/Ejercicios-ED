# Escribe un programa que cuente cuántos números positivos se ingresan en un
# vector de 8 elementos.

numeros = []

for i in range(8):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

contador_positivos = 0

for numero in numeros:
    if numero > 0:
        contador_positivos += 1

print(f"Se ingresaron {contador_positivos} números positivos.")