#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = int(input("Temperatura em celsius: "))
fahrenheit = (celsius/5*9)+32

print(f"\n{20*'='}\nTemperatura em Fahrenheit: {fahrenheit:.2f}")

