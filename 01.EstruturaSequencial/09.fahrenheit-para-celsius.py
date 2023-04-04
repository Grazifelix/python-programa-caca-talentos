# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
# Graziela Felix
# 04/04/23

fahrenheit = int(input("Temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit-32) / 9)

print(f"Temperatura em Celcius: {celsius:.2f}")
