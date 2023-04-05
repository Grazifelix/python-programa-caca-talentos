# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# Graziela Felix
# 05/04/23

valor = float(input("Digite um valor: "))
if valor < 0:
    print("Este valor é negativo.")
elif valor == 0:
    print("O valor zero é neutro, não é positivo nem negativo.")
else:
    print("Este valor é positivo.")
