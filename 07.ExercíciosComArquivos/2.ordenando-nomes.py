#Escreva um programa que leia um arquivo com um conjunto de nomes (1
# por linha). O programa deve ordenar os nomes e gerar um novo arquivo com os nomes ordenados.
# Graziela Felix
# 27/11/22

nomes = open("0.arquivos-utilizados/nomes")
lista_nomes = [x for x in nomes]
lista_nomes = sorted(lista_nomes)

nomes_ordenados = open("nomes-ordenados.txt", 'x')
nomes_ordenados.writelines(lista_nomes)
nomes_ordenados.close()

print("Arquivo com nomes ordenados gerado com sucesso")


