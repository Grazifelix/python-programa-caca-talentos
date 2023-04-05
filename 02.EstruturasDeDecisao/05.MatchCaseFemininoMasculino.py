# Faça um Programa que verifique se uma letra digitada é "F" ou "M" utilizando o Match Case.
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Graziela Felix
# 05/04/23

sexo = input("Selecione as opções:\nF - Feminino\nM - Masculino\n")
match sexo:
    case 'F':
        print("F - Feminino")
    case 'M':
        print("M - Masculino")
    case other:
        print("Sexo Inválido")



