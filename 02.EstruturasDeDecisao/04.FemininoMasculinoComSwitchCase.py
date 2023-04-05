# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
#NOTA: Switch Case não existe em python, mas ela pode ser criada com dicionario
# Graziela Felix
# 05/04/23

def switchCase(argumento):
    switcher = {
        'F': "F - Feminino",
        'M': "M - Masculino"
    }

    return switcher.get(argumento, "Sexo inválido")

if __name__ == '__main__':
    argumento = input()
    print(switchCase(argumento))
