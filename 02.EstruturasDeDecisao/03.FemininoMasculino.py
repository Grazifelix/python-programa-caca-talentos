# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Graziela Felix
# 05/04/23

sexo = input()
if sexo == 'F':
    print(f"{sexo=} - Feminino")
elif sexo == 'M':
    print(f"{sexo=} - Masculino")
else:
    print(f"{sexo=} - Sexo Inválido")
