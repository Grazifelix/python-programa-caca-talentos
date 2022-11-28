#  Faça um programa que escreve uma frase digitada pelo usuário em um arquivo.
#  Em seguida o programa de ler e imprimir o conteúdo desse arquivo
# Graziela Felix
# 27/11/22

input_user = open("arquivo.txt", "w")
input_user.write(input("Digite uma frase: "))
input_user.close()

input_user = open("arquivo.txt")
print(input_user.read())
input_user.close()
