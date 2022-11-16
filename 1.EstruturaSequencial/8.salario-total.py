# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# Graziela Maria
# 16/11/22

valor_hora = float(input("Valor ganhado por hora de trabalho: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
print(f"Valor total do salário: \033[44m {valor_hora*horas_trabalhadas} \u001b[m")
